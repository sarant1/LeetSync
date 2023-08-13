class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        time = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                if grid[r][c] == 1:
                    fresh += 1
        
        direction = [[1, 0],[-1, 0],[0, -1], [0, 1]]
        while q and fresh > 0:
            time += 1
            for o in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direction:
                    row, col = r+dr,c+dc

                    if (row < 0 or row >= len(grid)) or (col < 0 or col >= len(grid[0])) or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    fresh -= 1
                    q.append([row, col])
        return time if fresh == 0 else -1 

            
