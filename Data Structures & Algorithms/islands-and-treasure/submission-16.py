from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        treasure = []
        ROWS,COLS = len(grid),len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    treasure.append([i,j])
        
        queue = deque(treasure)

        distance = 1
        while queue:
            len_queue = len(queue)
            for _ in range(len_queue):
                i,j = queue.popleft()
                if i > 0 and grid[i - 1][j] == 2147483647:
                    grid[i - 1][j] = distance
                    queue.append([i-1,j])
                if j > 0 and grid[i][j - 1] == 2147483647:
                    grid[i][j - 1] = distance
                    queue.append([i,j - 1])
                if j < COLS - 1 and grid[i][j + 1] == 2147483647:
                    grid[i][j + 1] = distance
                    queue.append([i,j + 1])
                if i < ROWS - 1 and grid[i + 1][j] == 2147483647:
                    grid[i + 1][j] = distance
                    queue.append([i+1,j])
            distance += 1
        
                    
            

        
