"""
Write tests for 2_python_part_2/task_read_write.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""

from part2.task_read_write import read_files
import tempfile
import os


def test_create_files():
    expected = "80, 37, 15, 14, 99, 99, 59, 90, 69, 39, 67, 91, 74, 40, 32, 82, 48, 1, 95, 66"
    numbers = [80, 37, 15, 14, 99, 99, 59, 90, 69,
               39, 67, 91, 74, 40, 32, 82, 48, 1, 95, 66]
    # temporary directory
    with tempfile.TemporaryDirectory(dir=os.getcwd()) as tmpdir:
        os.mkdir(str(tmpdir)+"/files")
        os.chdir(str(tmpdir)+"/files")
        # creating files
        for i in range(1, len(numbers)+1):
            with open("file_"+str(i)+".txt", 'w') as file:
                file.write(str(numbers[i-1]))
        # function which we test
        read_files(str(tmpdir))
        # readind output from results.txt
        with open("result.txt", 'r') as file2:
            output = file2.read()
    assert output == expected