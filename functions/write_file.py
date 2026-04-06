from pathlib import Path

def write_file(working_directory, file_path, content):
    abs_working_dir = Path(working_directory).resolve()
    abs_file_path = (abs_working_dir / file_path).resolve()
    try:
        abs_file_path.relative_to(abs_working_dir)
    except ValueError:
        return f'Error: "{file_path}" is not in the working directory'
    
    parent_dir = abs_file_path.parent
    try:
        parent_dir.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        return f"Could not create parent dirs: {parent_dir} = {e}"
    try:
        with abs_file_path.open('w', encoding="utf-8") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Failed to write to file: {file_path}, {e}"
    

# Groq tool schema: must be in OpenAI function format
schema_write_file = {
    "name": "write_file",
    "description": "Overwrites an existing file or writes to a new file if it doesn't exist (and creates required parent directories safely), constrained to the working directory.",
    "parameters": {
        "type": "object",
        "properties": {
            "working_directory": {
                "type": "string",
                "description": "The base working directory (optional)."
            },
            "file_path": {
                "type": "string",
                "description": "The path to the file to write.",
                "default": "."
            },
            "content": {
            "type": "string",
            "description": "The content to write to the file as a string.",
            "default": "."
            }
        },
        "required": ["file_path"]
    }
}