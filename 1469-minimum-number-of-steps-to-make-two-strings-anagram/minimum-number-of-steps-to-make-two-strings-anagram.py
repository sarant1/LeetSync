class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = [0] * 26
        ans = 0
        for i in range(len(s)):
            count[ord(s[i])-ord("a")]+=1
            count[ord(t[i])-ord("a")]-=1
        for i in range(26):
            ans+= max(0, count[i])
        return ans



        