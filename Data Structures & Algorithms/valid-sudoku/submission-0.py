class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isValidRows(board) and self.isValidCols(board) and self.isValidBoxes(board)

    def isValidRows(self, board: List[List[str]]) -> bool:
        for row in board:
            number_set: Set[str] = set()
            for char in row:
                if char == '.':
                    continue
                if char in number_set:
                    return False
                number_set.add(char)
        return True

    def isValidCols(self, board: List[List[str]]) -> bool:
        for col in range(len(board[0])):
            number_set: Set[str] = set()
            for row in range(len(board)):
                char = board[row][col]
                if char == '.':
                    continue
                if char in number_set:
                    return False
                number_set.add(char)
        return True

    def isValidBox(self, board: List[List[str]], row: int, col: int) -> bool:
        # Check 3x3 box
        number_set: Set[str] = set()
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                char = board[i][j]
                if char == '.':
                    continue
                if char in number_set:
                    return False
                number_set.add(char)
        return True

    def isValidBoxes(self, board: List[List[str]]) -> bool:
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                if not self.isValidBox(board, i, j):
                    return False
        return True

        