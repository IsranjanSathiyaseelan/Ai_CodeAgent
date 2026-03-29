import os

def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(os.path.join(working_directory, directory))
    if not abs_directory.startswith(abs_working_dir):
        return f'Error: "{directory}" is not in the working directory'

    final_response = ""
    contents = os.listdir(abs_directory)
    for content in contents:
        content_path = os.path.join(abs_directory, content)
        is_dir = os.path.isdir(content_path)
        size = os.path.getsize(content_path)
        final_response += f"- {content} files_size={size} bytes, is_dir={is_dir}\n"
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