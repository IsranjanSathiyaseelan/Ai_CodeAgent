from pathlib import Path

from functions.run_python_file import run_python_file

def main():
    working_dir = Path(__file__).resolve().parent / "calculator"
    print(run_python_file(str(working_dir), "main.py", ["3+5"]))

main()