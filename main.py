import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types


def generate_content(client, messages):
    # response from the gemini-2.0-flash-001 model
    text_response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )

    # Number of tokens in the prompt
    prompt_tokens = text_response.usage_metadata.prompt_token_count

    # Number of tokens in the response
    response_tokens = text_response.usage_metadata.candidates_token_count

    print(text_response.text)
    print(prompt_tokens)
    print(response_tokens)


def main():
    # Loads env key to genai
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    args = sys.argv[1:]

    # Check for user_prompt
    if not args:
        print("Your personal AI Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    # retrieves user prompt
    user_prompt = args[0]

    # stores a list of messages for Gemini to see the
    # whole conversation and answer with the whole context
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages)


if __name__ == "__main__":
    main()
