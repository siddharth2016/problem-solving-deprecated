# Find number of lucky days, where ith day is lucky if following numbers (all) are less than ith day value.
# [2, 3, 5, 10, 9] - 2 lucky days: 10 and 9 (4th and 5th elements)

def solve(arr, n):
    i = j = n-1
    count = 0
    while(i>=0):
        if (arr[i]>=arr[j]):
            j = i
            count += 1
        
        i -= 1
    
    return count

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(solve(arr, n))