"""Optional live Agent SDK lab with tools disabled; compare its runtime to the manual loop."""
import asyncio
import os
from labs.common import arguments, connection, ROOT

def options(model):
    from claude_agent_sdk import ClaudeAgentOptions
    return ClaudeAgentOptions(model=model, tools=[], max_turns=1,
        cwd=str(ROOT/'fixtures'), setting_sources=[],
        system_prompt='You are a workshop instructor. Answer only from the supplied synthetic catalog.')

async def run(model):
    from claude_agent_sdk import query, ResultMessage
    # Explicit empty tool list: this lab cannot use shell/read/write tools.
    async for message in query(prompt='Catalog: tools lab is 25 minutes and requires Messages lab. Explain it in two sentences.',
                               options=options(model)):
        if isinstance(message, ResultMessage):
            if message.is_error:
                raise RuntimeError(f'Agent failed: {message.subtype}')
            print(message.result)

if __name__ == '__main__':
    if arguments(__doc__).live:
        client, model = connection()
        client.close()
        asyncio.run(run(model))
    else:
        print('OFFLINE PLAN: Agent SDK owns the runtime; this restricted introduction has zero tools.')
        print('Extension: explain permission boundaries before enabling any read or write tool.')
