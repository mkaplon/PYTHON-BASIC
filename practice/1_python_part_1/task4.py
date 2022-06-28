"""
Write function which receives list of integers. Calculate power of each integer and
subtract difference between original previous value and it's power. For first value subtract nothing.
Restriction:
Examples:
    >>> calculate_power_with_difference([1, 2, 3])
    [1, 4, 7]  # because [1^2, 2^2 - (1^2 - 1), 3^2 - (2^2 - 2)]
"""
from typing import List


def calculate_power_with_difference(ints: List[int]) -> List[int]:
    #squares
    output=[i**2 for i in ints]
    for index in range(1, len(output)):
        output[index]-=output[index-1]-ints[index-1]
    return output

# print(calculate_power_with_difference([1, 2, 3]))
# print(calculate_power_with_difference([1,-1, -1]))
