"""
Write function which reads a number from input nth times.
If an entered value isn't a number, ignore it.
After all inputs are entered, calculate an average entered number.
Return string with following format:
If average exists, return: "Avg: X", where X is avg value which rounded to 2 places after the decimal
If it doesn't exists, return: "No numbers entered"
Examples:
    user enters: 1, 2, hello, 2, world
    >>> read_numbers(5)
    Avg: 1.67
    ------------
    user enters: hello, world, foo, bar, baz
    >>> read_numbers(5)
    No numbers entered

"""


def read_numbers(n: int) -> str:
    nums = []
    for i in range(n):
        num = input()
        try:
            nums.append(int(num))
        except ValueError:
            pass
    if len(nums) > 0:
        mean = sum(nums)/len(nums)
        return "Avg: {:.2f}".format(mean)
    else:
        return "No numbers entered"

# print(read_numbers(5))
