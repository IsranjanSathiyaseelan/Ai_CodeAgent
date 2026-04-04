# Ai_CodeAgent

Ai_CodeAgent is a small Python-based AI coding agent that uses the Groq API to answer user prompts and call local helper functions. The agent can list files, read file contents, write files, and run Python scripts inside a controlled workspace.

## What This Project Does

- Loads a `GROQ_API_KEY` from environment variables.
- Sends the user prompt to a Groq chat model.
- Lets the model choose from four available tools:
  - list files and directories
  - read file contents
  - write or update files
  - run a Python file with optional arguments
- Restricts file operations to the `calculator/` directory for safety.

The repository also includes a sample calculator app in `calculator/` that can be used to test the Python runner.

## Project Structure

- `main.py` - entry point for the AI agent.
- `call_function.py` - dispatches tool calls and keeps them inside the sandbox.
- `config.py` - shared configuration such as maximum file read size.
- `functions/` - helper functions and Groq tool schemas.
- `calculator/` - example Python package and sample app.
- `test.py` - simple local test script for the tool runner.

## Requirements

- Python 3.9 or newer
- A Groq API key
- `pip` or `uv` for dependency installation

## Setup

### 1. Clone the project

```bash
git clone <your-repo-url>
cd Ai_CodeAgent
```

### 2. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.venv\\Scripts\\Activate.ps1
```

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install the dependencies

The project uses `groq` and `python-dotenv` at runtime.

```bash
pip install groq python-dotenv
```

If you want to install from the project metadata, you can also use `uv`:

```bash
uv sync
```

### 4. Set your Groq API key

Create a `.env` file in the project root and add:

```env
GROQ_API_KEY=your_api_key_here
```

You can also set the variable directly in your shell session instead of using a `.env` file.

### 5. Run the agent

Pass your prompt as a command-line argument:

```bash
python main.py "List the files in the calculator folder"
```

If you want verbose token usage output, add `--verbose`:

```bash
python main.py --verbose "Read calculator/main.py"
```

## Running the Sample Calculator

The `calculator/` folder contains a separate example app that evaluates basic arithmetic expressions.

```bash
python calculator/main.py "3 + 5"
```

Expected output:

```text
+--------------------------+
| Expression: 3 + 5       |
| Result: 8               |
+--------------------------+
```

## Available Tools

The AI agent can call these functions:

- `get_files_info(directory)` - lists files and directories in a safe location.
- `get_file_content(file_path)` - reads a file up to the configured character limit.
- `write_file(file_path, content)` - writes or overwrites a file.
- `run_python_file(file_path, args)` - runs a Python file with optional CLI arguments.

All tool calls are limited to the `calculator/` workspace boundary.

## Notes

- The agent currently uses the Groq model `llama-3.3-70b-versatile`.
- File reads are capped by `MAX_CHARS` in `config.py`.
- The sandbox check prevents the tools from accessing paths outside `calculator/`.

## Example Workflow

1. Start the virtual environment.
2. Set `GROQ_API_KEY`.
3. Run `python main.py "Your request here"`.
4. Let the model choose a tool or answer directly.
5. Review the printed function result or final response in the terminal.
