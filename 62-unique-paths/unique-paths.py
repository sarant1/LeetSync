class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        count = 0
        dp = [[-1 for l in range(n)] for _ in range(m)] 

        def dfs(i, j):
            if i > m-1 or j > n-1:
                return 0
            if dp[i][j]  != -1:
                return dp[i][j]
            if i == m-1 and j == n-1:
                return 1
            dp[i][j] = dfs(i+1,j) + dfs(i,j+1) 
            return dp[i][j]
        return dfs(0, 0) 
            




        

            




                


        

