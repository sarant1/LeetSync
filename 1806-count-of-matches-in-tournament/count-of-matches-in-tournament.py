class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        def dfs(t):
            nonlocal ans
            if t <= 1:
                return
            if t % 2 == 0:
                matches = t // 2
                ans += matches
                dfs(matches)
            else:
                matches = (t-1) // 2
                ans += matches 
                dfs(matches+1)
        dfs(n)
        return ans
        


        