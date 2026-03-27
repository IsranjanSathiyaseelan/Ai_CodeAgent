import os
import sys
from dotenv import load_dotenv
from groq import Groq  
from functions.get_files_info import get_files_info

def main():
    load_dotenv()
    api_key = os.environ.get("GROQ_API_KEY")
    client = Groq(api_key=api_key)

    #list of command-line arguments
    if len(sys.argv) < 2:
        print("I need a prompt!")
        sys.exit(1)         #Stop the program immediately
    verbose_flag = False

    if "--verbose" in sys.argv:
        verbose_flag = True
        sys.argv.remove("--verbose")  # Remove so it doesn't go into the prompt

    prompt = " ".join(sys.argv[1:])

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    print(chat_completion.choices[0].message.content)

    if verbose_flag and hasattr(chat_completion, "usage") and chat_completion.usage:
        print("\n--- VERBOSE INFO ---")
        print(f"User Prompt: {prompt}")
        print(f"Prompt tokens: {chat_completion.usage.prompt_tokens}")
        print(f"Completion tokens: {chat_completion.usage.completion_tokens}")
        print(f"Total tokens: {chat_completion.usage.total_tokens}")

#print(get_files_info("calculator"))

main()