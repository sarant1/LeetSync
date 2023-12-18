class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[-1 for _ in range(len(triangle[i]))] for i in range(len(triangle))]
        def dfs(i, j, res):
            if i > len(triangle)-1:
                return res
            if dp[i][j] != -1:
                return dp[i][j] 
            first = triangle[i][j] + dfs(i+1, j, res)
            second = triangle[i][j] + dfs(i+1, j+1, res)
            res = min(first, second)
            dp[i][j] = res

            return dp[i][j]
        return dfs(0, 0, 0)



            
        