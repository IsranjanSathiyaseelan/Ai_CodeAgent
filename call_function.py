import pathlib
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

# Base working directory for all operations
WORKING_DIRECTORY = pathlib.Path.cwd() / "calculator"


def call_function(function_call_part):
    """
    Executes a function call object with a name and args dict.
    The working directory is fixed to 'calculator'.
    """

    function_name = function_call_part.name
    args = function_call_part.args

    # Map available functions
    available_functions = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "write_file": write_file,
        "run_python_file": run_python_file
    }

    if function_name not in available_functions:
        return f"Error: Unknown function '{function_name}'"

    func = available_functions[function_name]

    try:
        if function_name == "get_files_info":
            directory = args.get("directory", ".")
            target_path = (WORKING_DIRECTORY / directory).resolve()

            # Ensure path is inside calculator
            if WORKING_DIRECTORY not in target_path.parents and WORKING_DIRECTORY != target_path:
                return f"Error: '{directory}' is outside working directory!"

            print(f"Calling function: {function_name}({{'directory': '{directory}'}})")
            return func(str(WORKING_DIRECTORY), directory)

        elif function_name == "get_file_content":
            file_path = args.get("file_path", ".")
            target_path = (WORKING_DIRECTORY / file_path).resolve()

            if WORKING_DIRECTORY not in target_path.parents and WORKING_DIRECTORY != target_path:
                return f"Error: '{file_path}' is outside working directory!"

            print(f"Calling function: {function_name}({{'file_path': '{file_path}'}})")
            return func(str(WORKING_DIRECTORY), file_path)

        elif function_name == "write_file":
            file_path = args.get("file_path")
            content = args.get("content", "")
            target_path = (WORKING_DIRECTORY / file_path).resolve()

            if WORKING_DIRECTORY not in target_path.parents and WORKING_DIRECTORY != target_path:
                return f"Error: '{file_path}' is outside working directory!"

            print(f"Calling function: {function_name}({{'file_path': '{file_path}'}})")
            return func(str(WORKING_DIRECTORY), file_path, content)

        elif function_name == "run_python_file":
            file_path = args.get("file_path")
            args_list = args.get("args", [])
            target_path = (WORKING_DIRECTORY / file_path).resolve()

            if WORKING_DIRECTORY not in target_path.parents and WORKING_DIRECTORY != target_path:
                return f"Error: '{file_path}' is outside working directory!"

            print(f"Calling function: {function_name}({{'file_path': '{file_path}'}})")
            return func(str(WORKING_DIRECTORY), file_path, args_list)

    except Exception as e:
        return f"Error executing function '{function_name}': {e}"