class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tempT = "".join(sorted(t))
        tempS = "".join(sorted(s))
        return tempT == tempS
        
