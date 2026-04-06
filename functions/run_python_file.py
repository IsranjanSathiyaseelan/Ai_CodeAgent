import subprocess
import sys
from pathlib import Path

def run_python_file(working_directory: str, file_path: str, args=None):
    if args is None:
        args = []

    abs_working_dir = Path(working_directory).resolve()
    abs_file_path = (abs_working_dir / file_path).resolve()
    try:
        abs_file_path.relative_to(abs_working_dir)
    except ValueError:
        return f'Error: "{file_path}" is not in the working directory'
    if not abs_file_path.is_file():
        return f'Error: "{file_path}" is not a file'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python files.'
    
    try:
        final_args = [sys.executable, str(abs_file_path)]
        final_args.extend(args)
        output = subprocess.run(
            final_args,
            cwd=str(abs_working_dir), 
            timeout=30,
            capture_output=True,
            text=True
        )
        final_string = f"""
STDOUT: {output.stdout}
STDERR: {output.stderr} 
"""
        if output.stdout == "" and output.stderr == "":
            final_string = "No output produced."
        if output.returncode != 0:
            final_string += f"Process exited with code {output.returncode}"
        return final_string
    except Exception as e:
        return f'Error: executing Python file: {e}'


# Groq tool schema: must be in OpenAI function format
schema_run_python_file = {
    "name": "run_python_file",
    "description": "Runsa a python file with the  python3 interpreter. Accepts additional arguments CLI args as an optional array.",
    "parameters": {
        "type": "object",
        "properties": {
            "working_directory": {
                "type": "string",
                "description": "The base working directory (optional)."
            },
            "file_path": {
                "type": "string",
                "description": "The file to run, relative to the working directory.",
                "default": "."
            },
            "args": {
                "type": "array",   
                "items": {
                    "type": "string"
                },
                "description": "Optional CLI arguments",
                "default": []   
            }
        },
        "required": ["file_path"]
    }
}