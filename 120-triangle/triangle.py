class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ans = 0
        cache = {}
        def dfs(i, j, res):
            if i == len(triangle):
                return res 
            if (i, j) in cache:
                return cache[(i, j)]
            first = triangle[i][j] + dfs(i+1, j, res)
            second = triangle[i][j] + dfs(i+1, j+1, res)
            res = min(first, second)
            
            cache[(i, j)] = res

            return cache[(i, j)]  
        return dfs(0, 0, 0)

            
        