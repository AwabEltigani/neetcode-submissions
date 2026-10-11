class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        
        visited = set()
        ROWS,COLS = len(grid),len(grid[0])
        res = 0

        def dfs(r,c):
            if (r,c) in visited:
                return
            visited.add((r,c))
            left = dfs(r,c - 1) if c > 0 and grid[r][c - 1] == '1' else None
            right = dfs(r,c + 1) if c < COLS - 1 and grid[r][c+1] == '1' else None
            top = dfs(r - 1,c) if r > 0 and grid[r - 1][c] == '1' else None
            bottom = dfs(r + 1,c) if r < ROWS - 1 and grid[r + 1][c] == '1' else None
                    
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1' and (i,j) not in visited:
                    print(grid[i][j])
                    res += 1
                    dfs(i,j)

        return res

            


        