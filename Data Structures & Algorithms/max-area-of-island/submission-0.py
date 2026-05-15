from typing import Tuple

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def getExplorationCoordinates(i: int, j: int) -> List[Tuple[int, int]]:
            return [
                (i + 1, j),
                (i - 1, j),
                (i, j + 1),
                (i, j - 1),
            ]

        def dfs(i: int, j: int) -> int:
            if i < 0 or i >= len(grid):
                return 0
            if j < 0 or j >= len(grid[0]):
                return 0
            if grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            area = 1
            for neighbor_i, neighbor_j in getExplorationCoordinates(i, j):
                area += dfs(neighbor_i, neighbor_j)
            return area

        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        return max_area
