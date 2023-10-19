class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ans = res = ""
        g = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == "#":
                g += 1 
                continue
            if g == 0:
                res += s[i]
            else:
                g -= 1
        g = 0
        for i in range(len(t)-1,-1,-1):
            if t[i] == "#":
                g += 1
                continue
            if g == 0:
                ans+=t[i]
            else:
                g -= 1
        return ans == res




        




            



            


        