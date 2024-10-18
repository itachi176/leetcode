from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix) 
        col = len(matrix[0])
        l = 0 
        r = row * col - 1 
        while (l <= r):
            m = l + (r-l)//2
            row_index = m//col
            col_index = m%col
            if matrix[row_index][col_index] > target:
                r = m - 1
            elif matrix[row_index][col_index] < target:
                l = m + 1
            else:
                return True
        return False