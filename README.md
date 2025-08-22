# AI Agent in Python using Gemini API

## Overview
This LLM-powered command-line program is capable of reading, updating, and running Python code using the Gemini API. 

The technologies used in building this program are the following:
- Language: Python
- AI API: Gemini
- Text Editor: Neovim

This project was a learning project from (boot.dev)[https://www.boot.dev/courses/build-ai-agent-python] with many challenges that allowed to practice functional programming and debugging.

The learning goals of this project were to:
- Provide an introduction to multi-directory Python projects
- Understand how AI tools work under the hood
- Practice Python and functional programming

The goal was NOT to build an LLM from scratch, but to instead use a pre-trained LLM to build an AGENT from scratch.

Within this project, there were many concepts that were difficult to grasp and was my first introduction to them:

1. **Tokens**: Tokens are the currency of LLMs. They are the way the LLMs measure how much text they have to process. 1 token is roughly equivalent to 4 characters within an English word.
    - The `client.models.generate_content()` method uses two parameters `model` (the model name) and `contents` (the prompt to send the model) to generate  response.
    - The generated respones returns a `GenerateContentResponse` object with lots of properties attached to it including the `.text` property and the `usage_metadata` which has the `prompt_token_count` (tokens in the prompt) and the `candidates_token_count` (tokens in the response).

2. **Messages**: LLM APIs are not used in a "one-shot" manner, but rather as a conversation, which in turn has a history, and if we're able to keep track of that history, then with each new prompt, the model can see the entire conversation and respond within the larger context of the conversation.

3. **Tool Functions**: Since the goal was to build an LLM-powered command-line tool that can read, write, and run python code. We had to build the tool functions for the LLM to use. This way we use the LLM as a decision-making engine, but we're still the ones running the code. It works like this:
    - We tell the LLM which functions are available to it
    - We give it a prompt
    - It describes which function it wants to call, and what arguments to pass ti it
    - *We* call that function with the arguments it provided
    - We return the result to the LLM.

4. **System Prompts and Schemas**: The "system prompt" is a special prompt that goes at the beginning of the conversation that carries more weight than a typical user prompt. The system prompt sets the tone for the conversation, and can be used to:
    - Set the personality of the AI
    - Give instructions on how to behave
    - Provide context for the conversation
    - Set the "rules" for the conversation. The `types.FunctionDeclaration` method builds a schema for the pre-built function which tells the LLM *how* to use the function.

5. **Feedback Loop**: A key part of an "Agent" is that it can ontinuously use its tools to iterate on its own results.

### Helpful Links
- (Boot.dev)[boot.dev]
- (Google Gen AI SDK)[https://googleapis.github.io/python-genai/index.html]
