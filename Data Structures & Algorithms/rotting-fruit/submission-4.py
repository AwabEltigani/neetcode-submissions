from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()
        fresh_oranges = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                if grid[i][j] == 2:
                    queue.append((i,j))

        time = 0
        while queue:
            length_queue = len(queue)
            print(grid,length_queue)
            for _ in range(length_queue):
                i,j = queue.popleft()
                if i > 0:
                    if grid[i - 1][j] == 1:
                        grid[i-1][j] = 2
                        queue.append((i-1,j))
                if j > 0:
                    if grid[i][j - 1] == 1:
                        grid[i][j - 1] = 2
                        queue.append((i,j - 1))
                if j < len(grid[0]) - 1:
                    if grid[i][j + 1] == 1:
                        grid[i][j + 1] = 2
                        queue.append((i,j+1))
                if i < len(grid) - 1:
                    if grid[i + 1][j] == 1:
                        grid[i+1][j] = 2
                        queue.append((i+1,j))
            fresh_oranges -= len(queue)
            if len(queue) > 0:
                time += 1
        print(fresh_oranges)
        return time if fresh_oranges == 0 else -1
                
        