class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ROWS,COLS = n,n
        colSet = set()
        posDiag = set()
        negDiag = set()
        board = ["."*n for _ in range(n)]
        res = []
        default = "."*n 
        
        def dfs(cur_line):
            
            if cur_line == n:
                res.append(board.copy())
                return
            
            
                
            for j in range(COLS):
                col = j
                pos_diag = cur_line + j
                neg_diag = cur_line - j
                if (neg_diag not in negDiag) and (pos_diag not in posDiag) and (col not in colSet):
                    colSet.add(j)
                    posDiag.add(cur_line + j)
                    negDiag.add(cur_line - j)
                    board[cur_line] = "."*(j) + "Q" + "."*(COLS-j-1)
                    dfs(cur_line + 1)
                    board[cur_line] = default
                    posDiag.remove(cur_line + j)
                    negDiag.remove(cur_line - j)
                    colSet.remove(j)
        dfs(0)
        return res

        




        