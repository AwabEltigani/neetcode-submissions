class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seenRow = set()
        seenCol = set()
        seenBox = set()

        for i in range(9):#row
            for j in range(9):#col
                num = board[i][j]
                if num == ".":
                    continue
                pos =(i//3) * 3+(j//3)
                colPos = str(num) + "is in col" + str(j)
                boxPos = str(num) + "is in box" + str(pos)
                if boxPos in seenBox:
                    return False
                else:
                    seenBox.add(boxPos)

                if colPos in seenCol:
                    return False
                else:
                    seenCol.add(colPos)
                
                rowPos = str(num) + "is in row" + str(i)
                if rowPos in seenRow:
                    return False
                else:
                    seenRow.add(rowPos)
            
            
            
                
                    

        
        return True


           

        