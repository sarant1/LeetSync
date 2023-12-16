class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        charsS, charsT = [0] * 26, [0] * 26
        for i in range(len(s)):
            charsS[ord(s[i])-ord("a")]+=1
            charsT[ord(t[i])-ord("a")]+=1
        return charsS == charsT


        