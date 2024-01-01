class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0
        c, i = 0, 0
        while c < len(s) and i < len(g):
            if s[c] >= g[i]:
                c+=1
                i+=1
                ans+=1
            else:
                c+=1
        return ans
        