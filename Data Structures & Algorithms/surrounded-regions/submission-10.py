from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:

        queue = deque([])
        o_set = set()
        ROWS,COLS = len(board),len(board[0])

        for i in range(ROWS):
            if board[i][0] == 'O':
                queue.append([i,0])
                o_set.add((i,0))
        
        for j in range(COLS):
            if board[0][j] == 'O':
                queue.append([0,j])
                o_set.add((0,j))
        
        for k in range(ROWS):
            if board[k][COLS-1] == 'O':
                queue.append([k,COLS-1])
                o_set.add((k,COLS-1))
        
        for l in range(COLS):
            if board[ROWS - 1][l] == 'O':
                queue.append([ROWS-1,l])
                o_set.add((ROWS-1,l))
        
        while queue:
            length_queue = len(queue)
            for _ in range(length_queue):
                i,j = queue.popleft()
                if i > 0 and board[i-1][j] == 'O' and (i-1,j) not in o_set:
                    o_set.add((i-1,j))
                    queue.append([i-1,j])
                if i < ROWS - 1 and board[i+1][j] == 'O' and (i+1,j) not in o_set:
                    o_set.add((i+1,j))
                    queue.append([i+1,j])
                if j > 0 and board[i][j-1] == 'O' and (i,j-1) not in o_set:
                    o_set.add((i,j-1))
                    queue.append([i,j-1])
                if j < COLS - 1 and board[i][j+1] == 'O' and (i,j+1) not in o_set:
                    o_set.add((i,j+1))
                    queue.append([i,j+1])
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O' and (i,j) not in o_set:
                    board[i][j] = 'X'

        