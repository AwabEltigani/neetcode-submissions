from collections import deque
class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        
        queue_p = deque()
        set_p = set()
        queue_a = deque()
        set_a = set()
        visited_p = set()
        visited_a = set()

        ROWS,COLS = len(heights),len(heights[0])

        for i in range(COLS):
            queue_p.append([0,i])
            set_p.add((0,i))
            visited_p.add((0,i))
            
        for j in range(ROWS):
            queue_p.append([j,0])
            set_p.add((j,0))
            visited_p.add((j,0))
        
        for k in range(COLS):
            queue_a.append([ROWS - 1,k])
            set_a.add((ROWS-1,k))
            visited_a.add((ROWS-1,k))
        
        for l in range(ROWS):
            queue_a.append([l,COLS-1])
            visited_a.add((l,COLS-1))
            set_a.add((l,COLS-1))
        
        while queue_p:
            length = len(queue_p)
            for _ in range(length):
                i,j = queue_p.popleft()

                if (i-1,j) not in set_p:
                    if i > 0 and heights[i - 1][j] >= heights[i][j]:
                        set_p.add((i-1,j))
                        queue_p.append([i-1,j])
                
                if (i + 1,j) not in set_p:
                    if i < ROWS - 1 and heights[i + 1][j] >= heights[i][j]:
                        set_p.add((i+1,j))
                        queue_p.append([i+1,j])
                
                if (i,j + 1) not in set_p:
                    if j < COLS - 1 and heights[i][j + 1] >= heights[i][j]:
                        set_p.add((i,j + 1))
                        queue_p.append([i,j+1])
                
                if (i,j - 1) not in set_p:
                    if j > 0 and heights[i][j-1] >= heights[i][j]:
                        set_p.add((i,j-1))
                        queue_p.append([i,j-1])
        
        while queue_a:
            length = len(queue_a)
            for _ in range(length):
                i,j = queue_a.popleft()

                if (i-1,j) not in set_a:
                    if i > 0 and heights[i - 1][j] >= heights[i][j]:
                        set_a.add((i-1,j))
                        queue_a.append([i-1,j])
                
                if (i + 1,j) not in set_a:
                    if i < ROWS - 1 and heights[i + 1][j] >= heights[i][j]:
                        set_a.add((i+1,j))
                        queue_a.append([i+1,j])
                
                if (i,j + 1) not in set_a:
                    if j < COLS - 1 and heights[i][j + 1] >= heights[i][j]:
                        set_a.add((i,j + 1))
                        queue_a.append([i,j+1])
                
                if (i,j - 1) not in set_a:
                    if j > 0 and heights[i][j-1] >= heights[i][j]:
                        set_a.add((i,j-1))
                        queue_a.append([i,j-1])
        
        res = []
        for height in set_a:
            if height in set_p:
                res.append([height[0],height[1]])
        
        return res

        
                
        
            