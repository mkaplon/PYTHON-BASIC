"""
Write a function that makes a request to some url
using urllib. Return status code and decoded response data in utf-8
Examples:
     >>> make_request('https://www.google.com')
     200, 'response data'
"""
from re import M, S
from typing import Tuple
from urllib.request import urlopen
from unittest.mock import Mock, patch


def make_request(url: str) -> Tuple[int, str]:
    f = urlopen(url)
    return (f.getcode(), f.read().decode('utf-8'))


"""
Write test for make_request function
Use Mock for mocking request with urlopen https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 200
    >>> m.method2.return_value = b'some text'
    >>> m.method()
    200
    >>> m.method2()
    b'some text'
"""

@patch("task_5.urlopen")
def test_url(mock_url):
    m = Mock()
    m.getcode.return_value = 200
    m.read.return_value = b"test"
    mock_url.return_value = m
    assert make_request('https://www.google.com')[0] == 200
    assert make_request('https://www.google.com')[1] == "test"
    
