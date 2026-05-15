class Coordinate:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def __eq__(self, other):
        if isinstance(other, Coordinate):
            return self.row == other.row and self.col == other.col
        return False

    def __hash__(self):
        # Hash based on the same unique attribute used in __eq__
        return hash((self.row, self.col))


class Solution:
    def __init__(self):
        self.claimed_rows: Set[int] = set()
        self.claimed_cols: Set[int] = set()
        self.claimed_diagonals: Dict[Coordinate, int] = {}
        self.queen_placements: Set[Coordinate] = set()

    def solveNQueens(self, n: int) -> List[List[str]]:
        results: List[List[str]] = []
        self.placeNQueens(0, n, results)
        return results

    def getBoardStateFromQueens(self, n) -> List[str]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        for placement in self.queen_placements:
            board[placement.row][placement.col] = 'Q'
        return [''.join(row) for row in board]

    def placeNQueens(self, current_row: int, n: int, results: List[List[str]]) -> None:
        if current_row == n:
            results.append(self.getBoardStateFromQueens(n))
            return
        for col in range(n):
            placement_option = Coordinate(current_row, col)
            if self.isSpaceAvailable(placement_option):
                self.claimCoveredSpaces(placement_option, n)
                self.placeNQueens(current_row + 1, n, results)
                self.releaseCoveredSpaces(placement_option, n)
        return

    def isSpaceAvailable(self, placement: Coordinate) -> bool:
        if placement.row in self.claimed_rows:
            return False
        if placement.col in self.claimed_cols:
            return False
        if placement in self.claimed_diagonals:
            return False
        return placement not in self.queen_placements

    def getAllDiagonalCoordinatesForQueenPlacement(self, queen_placement: Coordinate, n: int) -> List[Coordinate]:
        results: List[Coordinate] = []
        # check upper left diagonal
        x, y = queen_placement.row - 1, queen_placement.col - 1
        while x > -1 and y > -1:
            results.append(Coordinate(x, y))
            x -= 1
            y -= 1
        # check lower left diagonal
        x, y = queen_placement.row + 1, queen_placement.col - 1
        while x < n and y > -1:
            results.append(Coordinate(x, y))
            x += 1
            y -= 1
        # check upper right diagonal
        x, y = queen_placement.row - 1, queen_placement.col + 1
        while x > -1 and y < n:
            results.append(Coordinate(x, y))
            x -= 1
            y += 1
        # check lower right diagonal
        x, y = queen_placement.row + 1, queen_placement.col + 1
        while x < n and y < n:
            results.append(Coordinate(x, y))
            x += 1
            y += 1
        return results

    def claimCoveredSpaces(self, queen_placement: Coordinate, n: int) -> None:
        self.queen_placements.add(queen_placement)
        self.claimed_rows.add(queen_placement.row)
        self.claimed_cols.add(queen_placement.col)
        # claim diagonals
        diagonals = self.getAllDiagonalCoordinatesForQueenPlacement(queen_placement, n)
        for diagonal in diagonals:
            if diagonal not in self.claimed_diagonals:
                self.claimed_diagonals[diagonal] = 0
            self.claimed_diagonals[diagonal] += 1
        return

    def releaseCoveredSpaces(self, queen_placement: Coordinate, n: int) -> None:
        self.queen_placements.discard(queen_placement)
        self.claimed_rows.discard(queen_placement.row)
        self.claimed_cols.discard(queen_placement.col)
        # release diagonals
        diagonals = self.getAllDiagonalCoordinatesForQueenPlacement(queen_placement, n)
        for diagonal in diagonals:
            self.claimed_diagonals[diagonal] -= 1
            if self.claimed_diagonals[diagonal] <= 0:
                del self.claimed_diagonals[diagonal]
        return