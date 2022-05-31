"""
Write function which receives line of space sepparated words.
Remove all duplicated words from line.
Restriction:
Examples:
    >>> remove_duplicated_words('cat cat dog 1 dog 2')
    'cat dog 1 2'
    >>> remove_duplicated_words('cat cat cat')
    'cat'
    >>> remove_duplicated_words('1 2 3')
    '1 2 3'
"""


def remove_duplicated_words(line: str) -> str:
    line_list = line.split(' ')
    unique_list=[]
    for el in line_list:
        if el not in unique_list:
            unique_list.append(el)
    new_line = ' '.join(unique_list)
    return new_line

# print(remove_duplicated_words('cat cat dog 1 dog 2'))
# print(remove_duplicated_words('cat cat cat'))
# print(remove_duplicated_words('1 2 3'))