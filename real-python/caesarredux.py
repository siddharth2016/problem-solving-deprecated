# caesarredux.py
""" Caesar Cipher Redux, without using standard library
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

def caesar_cipher(letter, n):
    table = string.ascii_lowercase[n:] + string.ascii_lowercase[:n]
    try:
        index = string.ascii_lowercase.index(letter)
        return table[index]
    except ValueError:
        return letter

if __name__ == "__main__":
    text = input("Enter text to cipher: ")
    n = int(input("Enter number to do cipher: "))
    mod_text = [caesar_cipher(letter, n) for letter in text]
    print("".join(mod_text))