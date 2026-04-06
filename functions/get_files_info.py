from pathlib import Path

def get_files_info(working_directory, directory="."):
    abs_working_dir = Path(working_directory).resolve()
    abs_directory = (abs_working_dir / directory).resolve()
    try:
        abs_directory.relative_to(abs_working_dir)
    except ValueError:
        return f'Error: "{directory}" is not in the working directory'

    final_response = ""
    contents = sorted(abs_directory.iterdir(), key=lambda path: path.name.lower())
    for content in contents:
        is_dir = content.is_dir()
        size = content.stat().st_size
        final_response += f"- {content.name} file_size={size} bytes, is_dir={is_dir}\n"
    return final_response

# Groq tool schema: must be in OpenAI function format
schema_get_files_info = {
    "name": "get_files_info",
    "description": "List files int the specified directory along with their sizes. constrained to the working direcctory.",
    "parameters": {
        "type": "object",
        "properties": {
            "working_directory": {
                "type": "string",
                "description": "The base working directory (optional)."
            },
            "directory": {
                "type": "string",
                "description": "The directory to list files from, relative to the working directory.",
                "default": "."
            }
        },
        "required": ["directory"]
    }
}