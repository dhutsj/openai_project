import requests
import argparse
import json


# reference API https://learn.microsoft.com/en-us/azure/cognitive-services/openai/reference#completions
key = ""
endpoint = ""


def main():
    """ Gather prompt content
    """
    parser = argparse.ArgumentParser(
        description='Gather content from prompt',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '--content',
        dest='content',
        default='',
        help='Your content for the prompt')

    args = parser.parse_args()

    headers = {"Content-Type": "application/json", "api-key": key}
    body = {"prompt": args.content, "max_tokens": 512}
    response = requests.post(endpoint, headers=headers, json=body)
    print(response.json()['choices'][0]['message']['content'])


if __name__ == "__main__":
    main()
