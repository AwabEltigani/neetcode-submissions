class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:

        ROWS,COLS = len(grid),len(grid[0])
        max_area = 0

        def dfs(i,j):
            if i < 0 or j < 0 or i > ROWS - 1 or j > COLS - 1 or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + dfs(i + 1,j) + dfs(i - 1,j) + dfs(i,j + 1) + dfs(i,j - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                max_area = max(max_area,dfs(r,c))
        
        return max_area
        