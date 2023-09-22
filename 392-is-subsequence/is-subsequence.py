class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        comp = ""
        curr = 0
        for letter in t:
            if letter == s[curr]:
                curr+=1
                comp+=letter
                if comp == s:
                    return True
        return False



            
        
        