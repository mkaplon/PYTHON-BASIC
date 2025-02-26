"""
Use function 'generate_words' to generate random words.
Write them to a new file encoded in UTF-8. Separator - '\n'.
Write second file encoded in CP1252, reverse words order. Separator - ','.

Example:
    Input: ['abc', 'def', 'xyz']

    Output:
        file1.txt (content: "abc\ndef\nxyz", encoding: UTF-8)
        file2.txt (content: "xyz,def,abc", encoding: CP1252)
"""


from __future__ import unicode_literals


def generate_words(n=20):
    import string
    import random

    words = list()
    for _ in range(n):
        word = ''.join(random.choices(
            string.ascii_lowercase, k=random.randint(3, 10)))
        words.append(word)
    return words

def create_files(file1, file2):
    words = generate_words()
    with open(file1, 'w', encoding="utf-8") as f1:
        f1.write("\n".join(words))
    words.reverse()
    with open(file2, 'w', encoding="cp1252") as f2:
        f2.write(",".join(words))


if __name__ == "__main__":
    create_files("file1.txt", "file2.txt")
