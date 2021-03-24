# Find Minimum Lights, a hackathon coding challenge

def min_lights(arr, n):
    dp = [-1]*n
    l = r = 0

    for i, val in enumerate(arr):
        l = max(i-val, 0)
        r = min(i+val, n)
        dp[l] = max(dp[l], r)

    count = 1
    nexti = 0
    ri = dp[0]

    for i, val in enumerate(dp):
        nexti = max(nexti, val)

        if(i == ri):
            count += 1
            ri = nexti
        
    return count

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(min_lights(arr, n))