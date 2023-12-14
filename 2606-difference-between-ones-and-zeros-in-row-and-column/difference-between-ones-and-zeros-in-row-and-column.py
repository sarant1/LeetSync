class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(len(grid)):
            cur_sum = 0
            for j in range(len(grid[i])):
                if not grid[i][j]:
                    grid[i][j] = -1
                cur_sum+=grid[i][j]
            grid[i].append(cur_sum)
        grid.append([])
        for i in range(len(grid[0])-1):
            cur_sum = 0
            for j in range(len(grid)-1):
                cur_sum+=grid[j][i]
            grid[-1].append(cur_sum)
        for i in range(len(grid)-1):
            ans.append([])
            for j in range(len(grid[0])-1):
                ans[i].append(grid[i][-1]+grid[-1][j])
        return ans

                


        