
def reverse_fibo_print(a, b, num):
    if (num>1):
        reverse_fibo_print(b, a+b, num-1)
    print(a, end=" ")

reverse_fibo_print(0, 1, 10)
print()
reverse_fibo_print(0, 1, 1)
print()
reverse_fibo_print(0, 1, 2)
print()
reverse_fibo_print(0, 1, 0)