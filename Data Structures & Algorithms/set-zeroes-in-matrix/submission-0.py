class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows_to_zero = set()
        cols_to_zero = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    rows_to_zero.add(row)
                    cols_to_zero.add(col)
        
        for row in rows_to_zero:
            for col in range(len(matrix[0])):
                matrix[row][col] = 0
        
        for col in cols_to_zero:
            for row in range(len(matrix)):
                matrix[row][col] = 0

        
        