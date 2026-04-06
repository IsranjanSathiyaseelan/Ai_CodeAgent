# Ai_CodeAgent

Ai_CodeAgent is a Python CLI coding agent powered by Groq. It can answer prompts directly or call local tools to inspect and modify files in a sandboxed directory.

## Features

- Loads `GROQ_API_KEY` from environment variables (or `.env`).
- Sends prompts to a Groq chat model.
- Exposes four local tools to the model:
  - list files and directories
  - read file contents
  - write/update files
  - run Python files with optional arguments
- Restricts all file operations to the `calculator/` directory.

## Project Structure

- `main.py`: agent entry point and Groq chat/tool call flow.
- `call_function.py`: validates and dispatches tool calls.
- `config.py`: shared constants (`MAX_CHARS`, etc.).
- `functions/`: tool implementations plus tool schemas.
- `calculator/`: sandboxed workspace and sample calculator app.
- `test.py`: quick local testing helper.

## Requirements

- Python 3.9+
- Groq API key
- `uv` (recommended) or `pip`

## Setup

### 1. Clone and enter the project

```bash
git clone <your-repo-url>
cd Ai_CodeAgent
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

With `uv`:

```bash
uv sync
```

Or with `pip`:

```bash
pip install -e .
```

### 4. Set your API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_api_key_here
```

## Run the Agent

Use one of these commands from the project root:

```bash
python main.py "List files in the calculator folder"
```

```bash
uv run python main.py "List files in the calculator folder"
```

Verbose token usage:

```bash
python main.py --verbose "Read pkg/calculator.py"
```

```bash
uv run python main.py --verbose "Read pkg/calculator.py"
```

Note: On Windows, `uv run main.py ...` may fail in some environments. Prefer `uv run python main.py ...`.

## Available Tools

- `get_files_info(directory)`: list files/directories under the sandbox.
- `get_file_content(file_path)`: read file content up to `MAX_CHARS`.
- `write_file(file_path, content)`: create/overwrite a file in the sandbox.
- `run_python_file(file_path, args)`: run a Python file in the sandbox.

All tool calls are constrained to `calculator/`.

## Run the Sample Calculator

```bash
python calculator/main.py "3 + 5"
```

## Notes

- Model: `llama-3.3-70b-versatile`.
- Tool-calling request uses Groq chat `tools`/`tool_choice` format.
- File reads are limited by `MAX_CHARS` in `config.py`.
