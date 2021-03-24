# https://www.hackerrank.com/challenges/sock-merchant/problem

'''
Input:

9
10 20 20 10 10 30 50 10 20

Output:

3

'''

from collections import defaultdict
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    mp = defaultdict(lambda: 0)
    oddCount = 0
    for i, val in enumerate(ar):
        mp[val] += 1
        oddCount += 1
        if mp[val] == 2:
            mp[val] = 0
            oddCount -= 2
    return (n-oddCount)//2