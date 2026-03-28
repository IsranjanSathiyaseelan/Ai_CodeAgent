# from Ai_CodeAgent.functions.write_file import write_file
# from functions.get_files_info import get_files_info
from functions.write_file import write_file

def main():
    working_dir = "calculator"
    print(write_file(working_dir, "lorem.txt", "wait, this isn't lorem ipsum"))
    print(write_file(working_dir, "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print(write_file(working_dir, "pkg2/temp.txt", "this should  be allowed"))

main()