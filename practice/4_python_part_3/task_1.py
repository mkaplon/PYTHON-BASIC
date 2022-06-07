"""
using datetime module find number of days from custom date to now
Custom date is a string with format "2021-12-24"
If entered string pattern does not match, raise a custom Exception
If entered date is from future, return negative value for number of days
    >>> calculate_days('2021-10-07')  # for this example today is 6 october 2021
    -1
    >>> calculate_days('2021-10-05')
    1
    >>> calculate_days('10-07-2021')
    WrongFormatException
"""
from datetime import datetime
import pytest

class WrongFormatException(Exception):
    """Exception raised when date is in the wrong format"""
    pass


def calculate_days(from_date: str) -> int:
    now = datetime.now()
    try:
        date_params = from_date.split('-')
        date_ints = [int(el) for el in date_params]
        date2 = datetime(*date_ints)
    except:
        raise WrongFormatException("Wrong format!")
    delta = now - date2
    return delta.days


"""
Write tests for calculate_days function
Note that all tests should pass regardless of the day test was run
Tip: for mocking datetime.now() use https://pypi.org/project/pytest-freezegun/
"""


def test_date_from_past(freezer):
    freezer.move_to('2010-01-01')
    assert calculate_days('2009-12-31') == 1

def test_date_from_future(freezer):
    freezer.move_to('2010-01-01')
    assert calculate_days('2010-01-02') == -1

def test_date_wrong_format():
    with pytest.raises(WrongFormatException) as e:
        calculate_days('10-10-2010')
    assert "Wrong format!" in str(e.value)
