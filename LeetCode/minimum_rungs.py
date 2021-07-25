from typing import List

class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        currRung = 0
        i = 0
        count = 0
        while i<len(rungs):
            nextRung = rungs[i]
            if (nextRung - currRung)>dist:
                count += (nextRung - currRung - 1)//dist
            currRung = nextRung
            i += 1
        return count