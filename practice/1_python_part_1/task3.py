"""
Write function which receives list of text lines (which is space separated words) and word number.
It should enumerate unique words from each line and then build string from all words of given number.
Restriction: word_number >= 0
Examples:
    >>> build_from_unique_words('a b c', '1 1 1 2 3', 'cat dog milk', word_number=1)
    'b 2 dog'
    >>> build_from_unique_words('a b c', '', 'cat dog milk', word_number=0)
    'a cat'
    >>> build_from_unique_words('1 2', '1 2 3', word_number=10)
    ''
    >>> build_from_unique_words(word_number=10)
    ''
"""
from typing import Iterable


def build_from_unique_words(*lines: Iterable[str], word_number: int) -> str:
    if (word_number>=0):
        #text lines into lists
        a=[i.split() for i in lines]
        output_list=[]
        for text_line in a:
            try:
                #remaining unique values
                text_line = [text_line[i] for i in range(len(text_line)) if i==text_line.index(text_line[i])]
                if text_line[word_number]!='':
                    output_list.append(text_line[word_number])
            except IndexError:
                pass
        return(" ".join(output_list))



# print(build_from_unique_words('a b c', '1 1 1 2 3', 'cat dog milk', word_number=1))
# print(build_from_unique_words('a b c', '', 'cat dog milk', word_number=0))
# print(build_from_unique_words('1 2', '1 2 3', word_number=10))
# print(build_from_unique_words(word_number=10))