"""

Job-A-Thon Internship Question - June, 2021

Problem Statement:
There are  coins kept in a line. Each coin has two sides - one is colored gold and the other silver. You can flip two adjacent coins any number of times. You need to make the gold-colored side of every coin facing up. You are given the initial status of coins in a binary string  where '1' represents the gold side facing up and '0' represents the silver side facing up. If it is possible to make the gold-colored side of every coin facing up, return "Yes", otherwise return "No".

Input:
N = 8, s = "11001100"
Output:
Yes
Explanation: 
Flipping 3rd and 4th coin together and 7th 
and 8th coin together will do the task.

Input:
N = 8, s = "10010100"
Output:
No
Explanation: 
It is not possible to make the gold 
colored side of every coin facing up.

"""


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
