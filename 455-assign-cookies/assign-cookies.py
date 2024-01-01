class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0
        c = 0
        for i in range(min(len(s),len(g))):
            while c < len(s) and s[c] < g[i]:
                c+=1
            if c == len(s):
                break
            if g[i] <= s[c]:
                ans+=1 
                c+=1
        return ans
        