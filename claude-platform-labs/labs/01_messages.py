"""Teach the smallest request, response blocks, usage, and stop reason."""
from labs.common import arguments, connection, text_of, require_complete

def run(client, model):
    response = client.messages.create(
        model=model, max_tokens=180,
        system='You are a patient technical instructor. Use one concrete example.',
        messages=[{'role': 'user', 'content': 'Explain an API to a new technical seller in 60 words.'}],
    )
    require_complete(response)
    return {'answer': text_of(response), 'usage': response.usage.model_dump(),
            'request_id': getattr(response, '_request_id', None)}

if __name__ == '__main__':
    args = arguments(__doc__)
    if args.live:
        print(run(*connection()))
    else:
        print('OFFLINE ILLUSTRATION: An API is a defined way for programs to request work or data.')
        print('Exercise: explain why max_tokens limits output, not the size of the user input.')
