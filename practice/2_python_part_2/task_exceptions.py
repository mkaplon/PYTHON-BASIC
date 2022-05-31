"""
Write a function which divides x by y.
If y == 0 it should print "Division by 0" and return None
elif y == 1 it should raise custom Exception with "Deletion on 1 get the same result" text
else it should return the result of division
In all cases it should print "Division finished"
    >>> division(1, 0)
    Division by 0
    Division finished
    >>> division(1, 1)
    Division finished
    DivisionByOneException("Deletion on 1 get the same result")
    >>> division(2, 2)
    1
    Division finished
"""
from decimal import DivisionByZero
import typing


class CustomException(Exception):
    """Exception raised when y=1"""
    pass


def division(x: int, y: int) -> typing.Union[None, int]:
    try:
        if(y == 1):
            raise CustomException()
        return x/y
    except ZeroDivisionError:
        print("Division by 0")
    except CustomException:
        print("Deletion on 1 get the same result")
    finally:
        print("Division finished")

# print(division(1,0))
# print(division(1,1))
# print(division(2,2))
