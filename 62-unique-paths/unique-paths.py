class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        def dfs(x, y):
            if x < 0 or y < 0 or x>=m or y>=n:
                return 0
            if dp[x][y] != -1:
                return dp[x][y]
            if x==m-1 and y==n-1:
                return 1
            total = dfs(x+1,y) + dfs(x,y+1)
            dp[x][y] = total
            return total
        print(dp)
        return dfs(0,0)
        

            




                


        

