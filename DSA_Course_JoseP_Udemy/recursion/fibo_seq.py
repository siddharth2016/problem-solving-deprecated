def rec_fibo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return rec_fibo(n-1) + rec_fibo(n-2)

print(rec_fibo(4))

def it_fibo(n):
    f = 0
    s = 1
    if n==1:
        return f
    for _ in range(3, n+1):
        f, s = s, f+s
    return s

print(it_fibo(4), it_fibo(2), it_fibo(3), it_fibo(6), it_fibo(10))

cache = [None]*100
def dy_fibo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    if cache[n]:
        return cache[n]
    cache[n] = dy_fibo(n-1) + dy_fibo(n-2)
    return cache[n]

print(dy_fibo(5))
print(cache)
print(dy_fibo(10))
print(cache)
print(dy_fibo(55))
print(cache)