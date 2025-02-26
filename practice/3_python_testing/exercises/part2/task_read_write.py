"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""
import os, re

def read_files(directory: str):
    os.chdir(directory)
    all_values = []
    files_number = sum([bool(re.search(r"^file_(\d)+\.txt$", file)) for file in os.listdir("files")])
    for i in range(1, files_number + 1):
        with open("files/file_{}.txt".format(i), 'r') as file:
            all_values.append(file.read())
    output = ', '.join(all_values)
    with open("result.txt", 'w') as file2:
        file2.write(output)

if __name__ == "__main__":
    read_files(os.getcwd())

