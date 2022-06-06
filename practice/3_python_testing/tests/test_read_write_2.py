"""
Write tests for 2_python_part_2/task_read_write_2.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""

from part2.task_read_write_2 import create_files
from unittest.mock import patch


@patch("part2.task_read_write_2.generate_words", return_value=['abc', 'def', 'xyz'])
def test_read_write_2(mock_generate_words, tmpdir):

    file1 = tmpdir + "/file1.txt"
    file2 = tmpdir + "/file2.txt"
    create_files(file1, file2)

    with open(file1, 'r', encoding="utf-8") as f1:
        assert f1.read() == "abc\ndef\nxyz"
    with open(file2, 'r', encoding="cp1252") as f2:
        assert f2.read() == "xyz,def,abc"

    
