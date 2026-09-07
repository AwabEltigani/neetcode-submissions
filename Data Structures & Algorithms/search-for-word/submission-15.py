class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        first_char = word[0]
        visited = set()
        ROWS,COLS = len(board),len(board[0])
        

        def find_word(i,j,k):

            if k == len(word):
                return True
            
            if i < 0 or j < 0 or i > ROWS - 1 or j > COLS - 1 or (i,j) in visited or word[k] != board[i][j]:
                return False
            
            visited.add((i,j))
            
            res = find_word(i,j+1,k+1) or find_word(i + 1,j,k+1) or find_word(i - 1,j,k+1) or find_word(i,j - 1,k+1)

            visited.remove((i,j))

            return res
            

            
        
            

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == first_char:
                    found_word = find_word(i,j,0)
                    if found_word:
                        return True
        
        return False
        

                