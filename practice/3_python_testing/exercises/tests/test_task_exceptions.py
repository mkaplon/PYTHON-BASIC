"""
Write tests for division() function in 2_python_part_2/task_exceptions.py
In case (1,1) it should check if exception were raised
In case (1,0) it should check if return value is None and "Division by 0" printed
If other cases it should check if division is correct

TIP: to test output of print() function use capfd fixture
https://stackoverflow.com/a/20507769
"""

import pytest, unittest
from part2.task_exceptions import division, CustomException

def test_division_ok(capfd):
    division(2,5)
    out, err = capfd.readouterr()
    assert out == "Division finished\n"
    assert 2/5 == division(2,5)


def test_division_by_zero(capfd):
    division(1, 0)
    out, err = capfd.readouterr()
    assert out == "Division by 0\nDivision finished\n"
    assert division(1,0) is None


def test_division_by_one(capfd):
    with pytest.raises(CustomException) as e:
        division(1, 1)
    assert "Deletion on 1 get the same result" in str(e.value)
