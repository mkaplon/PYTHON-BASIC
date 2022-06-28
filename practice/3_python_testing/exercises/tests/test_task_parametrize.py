"""
Write a parametrized test for two functions.
The functions are used to find a number by ordinal in the Fibonacci sequence.
One of them has a bug.

Fibonacci sequence: https://en.wikipedia.org/wiki/Fibonacci_number

Task:
 1. Write a test with @pytest.mark.parametrize decorator.
 2. Find the buggy function and fix it.
"""

import pytest

def fibonacci_1(n):
    if n==0:
        return 0
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b


def fibonacci_2(n):
    fibo = [0, 1]
    for i in range(2, n+1):
        fibo.append(fibo[i-1] + fibo[i-2])
    return fibo[n]

numbers=[
    ('f1', 0, 0),
    ('f1', 1, 1),
    ('f1', 2, 1),
    ('f1', 13, 233),
    ('f2', 0, 0),
    ('f2', 1, 1),
    ('f2', 2, 1),
    ('f2', 13, 233)
]

@pytest.mark.parametrize('func, n, output', numbers)
def test_1(func, n, output):
    if func == 'f1':
        assert fibonacci_1(n) == output
    if func == 'f2':
        assert fibonacci_2(n) == output

