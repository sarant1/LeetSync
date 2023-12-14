class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def dfs(x, y, res):
            if (x, y) in cache:
                return cache[(x, y)]
            if x == m - 1 and y == n - 1:
                return 1
            if x >= m or y >= n:
                return 0
            res = dfs(x + 1, y, res) + dfs(x, y+1, res)
            cache[(x, y)] = res
            return res 
        return dfs(0, 0, 0)
