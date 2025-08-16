import os
import sys

from dotenv import load_dotenv
from google import genai


def main():
    args = sys.argv[1:]

    if not args:
        print("Your personal AI Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = args[0]

    # response from the gemini-2.0-flash-001 model
    text_response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=user_prompt
    )

    # Number of tokens in the prompt
    prompt_tokens = text_response.usage_metadata.prompt_token_count

    # Number of tokens in the response
    response_tokens = text_response.usage_metadata.candidates_token_count

    print(text_response.text)
    print(prompt_tokens)
    print(response_tokens)


if __name__ == "__main__":
    main()
