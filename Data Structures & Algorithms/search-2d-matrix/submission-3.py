class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        '''
        given a matrix and an integer target 
        to find a integer if it exsits in the matrix is by checking the first integer in each array 
        if it greater than the target then that means it cannot exsit in that row
        if it is less than or equal to then it might exist 
        we just go into that row and implement binary search 
        time -> O(log(m*n)) m is the number of rows and n is the number of columns
        space -> O(1) we dont use space 
        '''

        rows = len(matrix) - 1

        while rows > -1:
            if target < matrix[rows][0]:
                rows = rows - 1
            else:
                break
            
        if rows == -1:
            return False
        
        l = 0
        r = len(matrix[0]) - 1

        while r >= l:
            m = (r + l)//2
            if target == matrix[rows][m]:
                return True
            elif target >= matrix[rows][m]:
                l = m + 1
            else:
                r = m - 1
        
        return False
        
