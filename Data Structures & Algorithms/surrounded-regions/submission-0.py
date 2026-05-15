class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def markUncapturablePieces(i: int, j: int) -> None:
            if i < 0 or i >= len(board):
                return
            if j < 0 or j >= len(board[0]):
                return
            if board[i][j] != 'O':
                return
            board[i][j] = 'U'
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                markUncapturablePieces(i + dx, j + dy)

        # Check first and last rows
        for row in range(len(board)):
            if board[row][0] == 'O':
                markUncapturablePieces(row, 0)
            if board[row][-1] == 'O':
                markUncapturablePieces(row, len(board[0]) - 1)

        for col in range(len(board[0])):
            if board[0][col] == 'O':
                markUncapturablePieces(0, col)
            if board[-1][col] == 'O':
                markUncapturablePieces(len(board) - 1, col)

        uncapturable = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'U':
                    uncapturable.add((i, j))
        for i, j in uncapturable:
            board[i][j] = 'O'
        
            

        