class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        vals, valt = 0, ord(t[-1]) 
        for i in range(len(t)-1): 
           vals += ord(s[i]) 
           valt += ord(t[i])
        return chr(valt-vals) 
            







        