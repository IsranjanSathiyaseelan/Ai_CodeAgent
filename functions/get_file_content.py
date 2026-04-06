from pathlib import Path

from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_working_dir = Path(working_directory).resolve()
    abs_file_path = (abs_working_dir / file_path).resolve()
    try:
        abs_file_path.relative_to(abs_working_dir)
    except ValueError:
        return f'Error: "{file_path}" is not in the working directory'
    if not abs_file_path.is_file():
        return f'Error: "{file_path}" is not a file'
    
    file_content_string = ""
    try:
        with abs_file_path.open("r", encoding="utf-8") as f:
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