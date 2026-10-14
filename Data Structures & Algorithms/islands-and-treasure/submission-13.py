from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i,j))
        trips = 1
        while queue:
            queue_length = len(queue)
            for _ in range(queue_length):
                i,j = queue.popleft()
                if i > 0 and grid[i - 1][j] == 2147483647:
                    grid[i - 1][j] = trips
                    queue.append((i-1,j))
                if i < len(grid) - 1 and grid[i + 1][j] == 2147483647:
                    grid[i + 1][j] = trips
                    queue.append((i + 1,j))
                if j > 0 and grid[i][j - 1] == 2147483647:
                    grid[i][j - 1] = trips
                    queue.append((i,j-1))
                if j < len(grid[0]) - 1 and grid[i][j + 1] == 2147483647:
                    grid[i][j + 1] = trips
                    queue.append((i,j+1))
                
            trips += 1

        