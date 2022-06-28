"""
Write function which executes custom operation from math module
for given arguments.
Restrition: math function could take 1 or 2 arguments
If given operation does not exists, raise OperationNotFoundException
Examples:
     >>> math_calculate('log', 1024, 2)
     10.0
     >>> math_calculate('ceil', 10.7)
     11
"""
import math, pytest


class OperationNotFoundError(Exception):
    pass


def math_calculate(function: str, *args):
    if function not in dir(math):
        raise OperationNotFoundError("Operation not found")
    if len(args)>2 or len(args)==0:
        raise Exception("Wrong number of arguments")

    int_args = [str(el) for el in args]
    arguments = ', '.join(int_args)
    operation = "math.{}({})".format(function, arguments)
    return eval(operation)


"""
Write tests for math_calculate function
"""
def test_one_argument():
    assert math_calculate('floor', 11.34) == 11

def test_two_arguments():
    assert math_calculate('log', 1024, 2) == 10

def test_operation_not_found_error():
    with pytest.raises(OperationNotFoundError) as e:
        math_calculate("pierwiastek", 140)
    assert "Operation not found" in str(e.value)

def test_wrong_number1():
    with pytest.raises(TypeError) as e:
        math_calculate("ceil", 10, 20)
    assert "takes exactly one argument" in str(e.value)

def test_wrong_number2():
    with pytest.raises(Exception) as e:
        math_calculate("floor", 10, 10, 10)
    assert "Wrong number of arguments" in str(e.value)
