def flipCoins(self, N, s):
        # Code here
        x = s[0]
        y = x
        for i in range(N-1):
            if y == '0':
                x = '1' if s[i+1] == '0' else '0'
            else:
                x = s[i+1]
            y = x
        return "Yes" if x == '1' else "No"
