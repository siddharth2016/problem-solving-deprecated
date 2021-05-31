
# The task is to print fibonacci series in reverse order.
# So, if the input n == 3, then output should be - 1 1 0
# Similarly, for n = 6, output - 5 3 2 1 1 0

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
