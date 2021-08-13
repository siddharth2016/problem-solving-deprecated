class Solution:
    def SubsequenceLength(self, s):
        maxLen = 0
        visited = {}
        start_i = 0
        
        for i in range(len(s)):
            
            if s[i] in visited:
                start_i = max(start_i, visited[s[i]] + 1)
            
            maxLen = max(maxLen, i - start_i + 1)
            visited[s[i]] = i
        
        return maxLen