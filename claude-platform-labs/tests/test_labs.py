import asyncio
import importlib
import json
from types import SimpleNamespace
import pytest
import httpx2
from anthropic import Anthropic
from anthropic.types import Message

def lab(name):
    return importlib.import_module('labs.' + name)

def response(content, stop='end_turn'):
    return {'id':'msg_fixture', 'type':'message', 'role':'assistant', 'model':'fixture-model',
            'content':content, 'stop_reason':stop, 'stop_sequence':None,
            'usage':{'input_tokens':10,'output_tokens':10}}

def mock_client(handler):
    return Anthropic(api_key='offline-test', max_retries=0,
        http_client=httpx2.Client(transport=httpx2.MockTransport(handler)))

def test_messages_actual_sdk_serialization():
    def handler(request):
        body=json.loads(request.content)
        assert body['max_tokens']==180 and body['messages'][0]['role']=='user'
        return httpx2.Response(200,json=response([{'type':'text','text':'An API connects programs.'}]))
    with mock_client(handler) as client:
        assert lab('01_messages').run(client,'fixture-model')['answer'].startswith('An API')

def test_structured_actual_sdk_parse():
    def handler(request):
        body=json.loads(request.content)
        assert body['output_config']['format']['type']=='json_schema'
        result={'category':'rate_limit','next_step':'Reduce concurrency.','needs_human':False}
        return httpx2.Response(200,json=response([{'type':'text','text':json.dumps(result)}]))
    with mock_client(handler) as client:
        assert lab('03_structured').classify(client,'fixture-model','429').category=='rate_limit'

def test_tool_protocol_and_result_ids():
    seen=[]
    def handler(request):
        body=json.loads(request.content); seen.append(body)
        if len(seen)==1:
            return httpx2.Response(200,json=response([{'type':'tool_use','id':'tool_1',
                'name':'lookup_lab','input':{'slug':'tools'}}],'tool_use'))
        result=body['messages'][-1]['content'][0]
        assert result['tool_use_id']=='tool_1' and not result['is_error']
        assert json.loads(result['content'])['minutes']==25
        return httpx2.Response(200,json=response([{'type':'text','text':'Requires Messages lab.'}]))
    with mock_client(handler) as client:
        assert lab('04_tool_loop').run(client,'fixture-model')=='Requires Messages lab.'
    assert len(seen)==2

def test_tool_boundary_and_limit():
    module=lab('04_tool_loop')
    with pytest.raises(ValueError): module.dispatch('run_shell',{'slug':'tools'})
    with pytest.raises(ValueError): module.dispatch('lookup_lab',{'slug':'tools','extra':'x'})
    message=Message.model_validate(response([{'type':'tool_use','id':'t','name':'lookup_lab',
                                               'input':{'slug':'tools'}}],'tool_use'))
    fake=SimpleNamespace(messages=SimpleNamespace(create=lambda **kw:message))
    with pytest.raises(RuntimeError,match='round limit'): module.run(fake,'fixture',2)

def test_incomplete_structured_response_rejected():
    def handler(request):
        return httpx2.Response(200,json=response([{'type':'text','text':'partial'}],'max_tokens'))
    with mock_client(handler) as client:
        with pytest.raises(Exception): lab('03_structured').classify(client,'fixture-model','429')

def test_eval_failures_are_counted():
    module=lab('05_evaluation')
    assert module.evaluate(lambda t:'other',[])['accuracy'] is None
    def broken(text): raise RuntimeError('fixture failure')
    assert module.evaluate(broken,[{'id':'x','text':'x','expected':'other'}])['passed']==0

def test_real_mcp_roundtrip():
    assert asyncio.run(lab('06_mcp').demo())['minutes']==25

def test_retry_budget_and_permanent_errors():
    delay=lab('07_reliability').retry_delay
    assert delay(401,0) is None
    assert delay(429,3) is None
    assert delay(429,0,retry_after=30)==30
    assert delay(500,2,random_value=.5)==2

def test_freshness_changed_and_unchanged():
    compare=lab('08_content_freshness').compare
    assert not compare({'a':1},{'a':1})['needs_human_review']
    assert compare({'a':1},{'a':2})['changed']==['a']

def test_agent_options_do_not_enable_tools():
    options=lab('09_agent_sdk').options('fixture-model')
    assert options.tools==[] and options.max_turns==1 and options.setting_sources==[]

def test_logs_reject_bad_shapes_and_nonfinite_numbers():
    analyze=lab('10_log_analyzer').analyze
    result=analyze(['[]','null','{"status":true}', '{"status":200,"latency_ms":"NaN"}',
                    '{"status":200,"latency_ms":-1}', '{"status":"429","latency_ms":"40"}'])
    assert result['valid']==1 and len(result['rejected'])==5
    assert result['error_rate']==1 and result['p95_ms']==40
    assert analyze([])['error_rate'] is None
