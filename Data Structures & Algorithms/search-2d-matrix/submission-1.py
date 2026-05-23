class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix) - 1
        col = len(matrix[0]) - 1
        rowFound = -1

        for i in range(rows,-1,-1):
            if target >= matrix[i][0]:
                rowFound = i
                break
        
        if rowFound == -1:
            return False

        arr = matrix[rowFound]
        
        l = 0
        r = col

        while r>=l:
            middle = math.floor((r+l)/2)
            if arr[middle] > target:
                r = middle - 1
            elif arr[middle] < target:
                l = middle + 1
            else:
                return True
        
        return False
        

