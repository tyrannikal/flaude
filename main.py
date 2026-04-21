import argparse
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    print("Hello from flaude!")

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    assert api_key is not None, "GEMINI_API_KEY is not set"

    client = genai.Client(api_key=api_key)

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    generate_response(client, messages, args.verbose)


def generate_response(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
    )
    assert response.usage_metadata is not None, (
        "Response usage_metadata is None, likely failed api call"
    )

    if verbose:
        print(f"User prompt: {messages[0].parts[0].text}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    print(f"Response: {response.text}")


if __name__ == "__main__":
    main()
