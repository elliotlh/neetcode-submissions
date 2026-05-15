from dataclasses import dataclass
@dataclass(frozen=True)
class Coordinate:
    i: int
    j: int

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        memo: Dict[Coordinate, int] = {}
        
        def getNeighbors(point: Coordinate) -> List[Coordinate]:
            neighbors: List[Coordinate] = []
            if point.i > 0:
                neighbors.append(Coordinate(point.i - 1, point.j))
            if point.i < len(matrix) - 1:
                neighbors.append(Coordinate(point.i + 1, point.j))
            if point.j < len(matrix[0]) - 1:
                neighbors.append(Coordinate(point.i, point.j + 1))
            if point.j > 0:
                neighbors.append(Coordinate(point.i, point.j - 1))
            return neighbors

        longest_path = 0
        def searchForLongestPath(point: Coordinate) -> int:
            nonlocal longest_path
            nonlocal memo
            if point.i < 0 or point.i >= len(matrix):
                return 0
            if point.j < 0 or point.j >= len(matrix[0]):
                return 0
            if point in memo:
                return memo[point]

            # this must be a best path, so we have to explore it
            longest_path_from_this_cell = 1
            for neighbor in getNeighbors(point):
                if matrix[neighbor.i][neighbor.j] > matrix[point.i][point.j]:
                    longest_path_from_this_cell = max(longest_path_from_this_cell, 1 + searchForLongestPath(neighbor))
            memo[point] = longest_path_from_this_cell
            return longest_path_from_this_cell

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                longest_path = max(longest_path, searchForLongestPath(Coordinate(i, j)))
        return longest_path


            