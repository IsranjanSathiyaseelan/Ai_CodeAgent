import os
import sys
import json
from dotenv import load_dotenv
from groq import Groq
from call_function import call_function

# Import function schemas for Groq
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file


def main():
    # Load environment variables
    load_dotenv()
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("Error: GROQ_API_KEY not set in environment.")
        sys.exit(1)

    client = Groq(api_key=api_key)

    # System prompt for AI agent
    system_prompt = """ 
You are a helpful AI coding agent.

when a user asks a question or make a request, make a function call plan . You can perform the followin operations:

- List files and directories
- Read file content of a file
- Write to a file (create or update)  
- Run a Python file with optional arguments 

All paths you provide should be relative to the working directory.You do not need to specify the working directory in your function calls as it  is automatically injected for security reasons.
"""

    # Get user prompt
    if len(sys.argv) < 2:
        print("I need a prompt!")
        sys.exit(1)

    prompt = " ".join(arg for arg in sys.argv[1:] if arg != "--verbose")

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ]

    # Call Groq for completion
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama-3.3-70b-versatile",
        functions=[
            schema_get_files_info,
            schema_get_file_content,
            schema_write_file,
            schema_run_python_file
        ],
        function_call="auto"
    )

    # Print token usage if --verbose flag is passed
    if "--verbose" in sys.argv:
        usage = getattr(chat_completion, "usage", None)
        if usage:
            print("\n--- Token Usage ---")
            print(f"Prompt tokens: {usage.prompt_tokens}")
            print(f"Completion tokens: {usage.completion_tokens}")
            print(f"Total tokens: {usage.total_tokens}")

    message = chat_completion.choices[0].message
    function_call_obj = getattr(message, "function_call", None)

    if function_call_obj:
        # Prepare function call object for helper
        class FunctionCallPart:
            def __init__(self, name, args):
                self.name = name
                self.args = args

        try:
            args_dict = json.loads(getattr(function_call_obj, "arguments", "{}"))
        except json.JSONDecodeError:
            print("Invalid JSON from model:", getattr(function_call_obj, "arguments", "{}"))
            args_dict = {}

        function_call_part = FunctionCallPart(
            name=getattr(function_call_obj, "name", None),
            args=args_dict
        )

        # Call the function via helper
        result = call_function(function_call_part)
        print("\n--- Function Result ---")
        print(result)

    else:
        # Normal AI response
        print("AI_Agent response:")
        print(message.content)


if __name__ == "__main__":
    main()