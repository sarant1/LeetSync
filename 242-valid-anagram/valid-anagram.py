class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letterMapS = {i:0 for i in range(26)}
        letterMapT = {i:0 for i in range(26)} 

        for i in range(len(s)):
            letterMapS[ord(s[i])-97]+=1
            letterMapT[ord(t[i])-97]+=1 
        if letterMapS == letterMapT:
            return True
        else:
            return False


