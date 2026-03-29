import os

from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: "{file_path}" is not in the working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: "{file_path}" is not a file'
    
    file_content_string = ""
    try:
        with open(abs_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) >= MAX_CHARS:
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return file_content_string
    except Exception as e:
        return f'Exception reading file: {e}"'
    

# Groq tool schema: must be in OpenAI function format
schema_get_file_content = {
    "name": "get_file_content",
    "description": "Gets the contents of the given file as a string, constrained to the working directory.",
    "parameters": {
        "type": "object",
        "properties": {
            "working_directory": {
                "type": "string",
                "description": "The base working directory (optional)."
            },
            "file_path": {
                "type": "string",
                "description": "the path to the file, from the working directory.",
                "default": "."
            }
        },
        "required": ["file_path"]
    }
}