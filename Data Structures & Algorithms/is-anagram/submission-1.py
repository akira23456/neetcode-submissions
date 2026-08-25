class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        matchS = {}
        matchT = {}

        for l in s:
            matchS[l] = matchS.get(l, 0) + 1
        
        for j in t:
            matchT[j] = matchT.get(j, 0) + 1
        
        if matchS == matchT:
            return True
        else: 
            return False