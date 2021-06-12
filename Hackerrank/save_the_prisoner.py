def saveThePrisoner(n, m, s):
    # Write your code here
    ans = (m-(n-s+1))%n
    return n if ans==0 else ans
