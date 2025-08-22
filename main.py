import os
import sys

from dotenv import load_dotenv

from google import genai
from google.genai import types

from config.prompts import system_prompt

from functions.call_functions import available_functions, call_function


def generate_content(client, messages, verbose):
    # response from the gemini-2.0-flash-001 model
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
    )

    # Number of tokens in the prompt
    prompt_tokens = response.usage_metadata.prompt_token_count

    # Number of tokens in the response
    response_tokens = response.usage_metadata.candidates_token_count

    if verbose:
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

    print("---------------AI Response---------------")
    # Based on prompt AI decides which function to call
    if response.function_calls:
        for call in response.function_calls:
            function_call_result = call_function(call, verbose)
            function_response = function_call_result.parts[0].function_response.response

            if not function_response:
                raise Exception("Error: no function response")

            print(f'-> {function_response}')
    else:
        print(response.text)


def main():
    # Loads env key to genai
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # Check for user_prompt
    args = []
    for arg in sys.argv:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("---------------Gemini AI Assistant---------------")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    # retrieves user prompt and checks for "--verbose" flag
    user_prompt = " ".join(args)
    verbose = "--verbose" in sys.argv

    if verbose:
        print("---------------User Prompt---------------")
        print(f"\nUser prompts: {user_prompt}")

    # stores a list of messages for Gemini to see the
    # whole conversation and answer with the whole context
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    # Generates content from Gemini AI
    generate_content(client, messages, verbose)


if __name__ == "__main__":
    main()
