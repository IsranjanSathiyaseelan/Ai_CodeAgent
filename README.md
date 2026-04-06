# Ai_CodeAgent

<<<<<<< HEAD
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
=======
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
>>>>>>> 0668201d8c0897438a844aef214116edc2c69861

```bash
git clone <your-repo-url>
cd Ai_CodeAgent
```

### 2. Create and activate a virtual environment

<<<<<<< HEAD
Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS/Linux:
=======
On Windows PowerShell:

```powershell
python -m venv .venv
.venv\\Scripts\\Activate.ps1
```

On macOS or Linux:
>>>>>>> 0668201d8c0897438a844aef214116edc2c69861

```bash
python3 -m venv .venv
source .venv/bin/activate
```

<<<<<<< HEAD
### 3. Install dependencies

With `uv`:
=======
### 3. Install the dependencies

The project uses `groq` and `python-dotenv` at runtime.

```bash
pip install groq python-dotenv
```

If you want to install from the project metadata, you can also use `uv`:
>>>>>>> 0668201d8c0897438a844aef214116edc2c69861

```bash
uv sync
```

<<<<<<< HEAD
Or with `pip`:

```bash
pip install -e .
```

### 4. Set your API key

Create a `.env` file in the project root:
=======
### 4. Set your Groq API key

Create a `.env` file in the project root and add:
>>>>>>> 0668201d8c0897438a844aef214116edc2c69861

```env
GROQ_API_KEY=your_api_key_here
```

<<<<<<< HEAD
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
=======
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
>>>>>>> 0668201d8c0897438a844aef214116edc2c69861

```bash
python calculator/main.py "3 + 5"
```

<<<<<<< HEAD
## Notes

- Model: `llama-3.3-70b-versatile`.
- Tool-calling request uses Groq chat `tools`/`tool_choice` format.
- File reads are limited by `MAX_CHARS` in `config.py`.
=======
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
>>>>>>> 0668201d8c0897438a844aef214116edc2c69861
