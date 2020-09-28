# integersums.py
""" Sum of Integers Up To n
    Write a function, add_it_up(), that takes a single integer as input
    and returns the sum of the integers from zero to the input parameter.

    The function should return 0 if a non-integer is passed in.
"""

def add_it_up(n: int) -> int:
    try:
        result = sum(range(int(n)+1))
    except ValueError:
        result = 0
    return result

if __name__ == "__main__":
    n = input()
    print(add_it_up(n))