class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0 for _ in range(len(triangle[-1])+1)] for i in range(n+1)]
        for i in range(n-1,-1,-1):
            for j in range(len(triangle[i])):
                dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1]) 
        return dp[0][0]



            
        