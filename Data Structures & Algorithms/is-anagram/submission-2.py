class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortS , sortT = {}, {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            sortS[s[i]] = 1 + sortS.get(s[i] ,0)
            sortT[t[i]] = 1 + sortT.get(t[i] ,0)

        for r in sortS:
            if sortS[r] != sortT.get(r,0):
                return False
        return True
