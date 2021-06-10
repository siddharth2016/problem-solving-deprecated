def getPairsCount(self, arr, n, k):
        # code here
        d = dict()
        count=0
        for val in arr:
            diff = k - val
            if diff in d:
                count += d[diff]
            if val not in d:
                d[val] = 0
            d[val] += 1
        return count
