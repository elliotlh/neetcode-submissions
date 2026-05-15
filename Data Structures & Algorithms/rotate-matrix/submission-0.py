"""
1. 2. 3. 4
5. 6. 7. 8
9. 10 11 12
13 14 15 16
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        num_iterations = n // 2
        for level in range(num_iterations):
            for offset in range(level, n - 1 - level):
                self.swap(matrix, level, offset)

    def swap(self, matrix: List[List[int]], level: int, offset: int) -> None:
        n = len(matrix)
        # Extract all the variables
        top_row = matrix[level][offset]
        right_col = matrix[offset][-1-level]
        bottom_row = matrix[-1-level][n-1-offset]
        left_col = matrix[n - 1 - offset][level]
        # top -> right
        matrix[offset][-1-level] = top_row
        # right -> bottom
        matrix[-1-level][n-1-offset] = right_col
        # bottom -> left
        matrix[n - 1 - offset][level] = bottom_row
        # left -> top
        matrix[level][offset] = left_col
