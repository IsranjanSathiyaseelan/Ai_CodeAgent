from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def main():
    working_dir = "calculator"
    
    # Print the content of main.py (this file exists)
    print(get_file_content(working_dir, "main.py"))

    # Print the content of calculator.py (this file exists in pkg folder)
    print(get_file_content(working_dir, "pkg/calculator.py"))

    # Test case: file does NOT exist
    # Should return an error: "pkg/notexists.py" is not a file
    print(get_file_content(working_dir, "pkg/notexists.py"))

    # Test case: file path is outside the working directory
    # Should return an error: "/bin/cat" is not in the working directory
    print(get_file_content(working_dir, "/bin/cat"))

    

    # root_contents = get_files_info(working_dir, ".")
    # print(root_contents)
    # pkg_contents = get_files_info(working_dir, "pkg")
    # print(pkg_contents)
    # pkg_contents = get_files_info(working_dir, "/bin")
    # print(pkg_contents)
    # pkg_contents = get_files_info(working_dir, "../")
    # print(pkg_contents)
    

main()