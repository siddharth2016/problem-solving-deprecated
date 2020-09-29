# caesar.py
""" Caesar Cipher
    A Caesar cipher is a simple substitution cipher in which each letter of the
    plain text is substituted with a letter found by moving n places down the
    alphabet. For example, assume the input plain text is the following:

        abcd xyz

    If the shift value, n, is 4, then the encrypted text would be the following:

        efgh bcd

    You are to write a function that accepts two arguments, a plain-text
    message and a number of letters to shift in the cipher. The function will
    return an encrypted string with all letters transformed and all
    punctuation and whitespace remaining unchanged.

    Note: You can assume the plain text is all lowercase ASCII except for
    whitespace and punctuation.
"""

import string

def caesar(plain_text: str, n: int) -> str:
    letters = string.ascii_lowercase
    mask = letters[(n%26):] + letters[:(n%26)]
    transtable = str.maketrans(letters, mask)
    return plain_text.translate(transtable)


if __name__ == "__main__":
    txt = input("Enter plain text: ")
    n = int(input("Enter n: "))
    print(caesar(txt, n))
