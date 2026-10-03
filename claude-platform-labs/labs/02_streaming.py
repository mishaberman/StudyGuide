"""Distinguish time to first text from total response latency."""
from time import perf_counter
from labs.common import arguments, connection, require_complete

def run(client, model):
    start = perf_counter()
    first_text = None
    with client.messages.stream(model=model, max_tokens=220,
            messages=[{'role': 'user', 'content': 'Give three tips for teaching tool use.'}]) as stream:
        for chunk in stream.text_stream:
            if chunk and first_text is None:
                first_text = perf_counter() - start
            print(chunk, end='', flush=True)
        final = stream.get_final_message()
    require_complete(final)
    print({'first_text_seconds': first_text, 'total_seconds': perf_counter() - start,
           'usage': final.usage.model_dump()})

if __name__ == '__main__':
    if arguments(__doc__).live:
        run(*connection())
    else:
        print('OFFLINE ILLUSTRATION: chunks -> visible text -> final message -> usage.')
        print('A stream can fail after showing partial text. Do not treat partial output as complete.')
