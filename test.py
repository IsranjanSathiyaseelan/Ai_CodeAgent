# from Ai_CodeAgent.functions.write_file import write_file
# from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file

def main():
    working_dir = "calculator"
    print(run_python_file(working_dir, "main.py", ["3+5"]))

main()