class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        cache = {}
        mod = 10 ** 9 + 7
        def dfs(moves, x, y):
            if moves == -1:
                return 0 
            if x < 0 or y < 0 or x >= m or y >= n:
                return 1
            if (x, y, moves) in cache:
                return cache[(x, y, moves)]
            res = (
                dfs(moves-1, x+1, y) +
                dfs(moves-1, x-1, y) +
                dfs(moves-1, x, y+1) +
                dfs(moves-1, x, y-1)  
            ) 
            cache[(x, y, moves)] = res
            return res 
        return dfs(maxMove, startRow, startColumn) % mod

        