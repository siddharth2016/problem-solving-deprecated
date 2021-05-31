
# The task is to print fibonacci series in reverse order.
# So, if the input num == 3, then output should be - 1 1 0
# Similarly, for num = 6, output - 5 3 2 1 1 0
# Given first 2 numbers of fibonacci series, a = 0, b = 1

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
