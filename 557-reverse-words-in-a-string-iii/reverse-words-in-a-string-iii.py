class Solution:
    def reverseWords(self, s: str) -> str:
        curr = ans = ""
        start = 0 
        for i in range(len(s)):
            if s[i] == " ":
                ans += curr[::-1]
                ans += " "
                curr = ""
            else:
                curr += s[i]
        ans += curr[::-1]
        return ans

        
        

            

        