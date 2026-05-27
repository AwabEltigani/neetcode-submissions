class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seen = set()

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                position_box = "num:" + num + "box: " + str(i//3) + " "  + str(j//3)
                position_row = "num:" + num + "row: " + str(i)
                position_col = "num:" + num + "col: " + str(j)
                if position_box in seen or position_row in seen or position_col in seen:
                    return False
                seen.add(position_box)
                seen.add(position_row)
                seen.add(position_col)
        
        return True
                
        