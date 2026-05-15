from enum import IntEnum
import collections
from typing import List


class GroundType(IntEnum):
    WATER = -1
    TREASURE = 0
    UNVISITED_LAND = 2147483647


class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == GroundType.TREASURE:
                    queue.append(Cell(i, j))

        depth = 0
        while queue:
            cells_at_depth = len(queue)
            for i in range(cells_at_depth):
                cell = queue.popleft()
                i, j = cell.i, cell.j
                if grid[i][j] == GroundType.UNVISITED_LAND:
                    grid[i][j] = depth
                queue.extend(self.getInboundNeighborsForCell(grid, cell))
            depth += 1
        return

    def getInboundNeighborsForCell(self, grid: List[List[int]], cell: Cell) -> List[Cell]:
        neighbors: List[Cell] = []
        i, j = cell.i, cell.j
        if i > 0 and grid[i - 1][j] == GroundType.UNVISITED_LAND:
            neighbors.append(Cell(i - 1, j))
        if i < len(grid) - 1 and grid[i + 1][j] == GroundType.UNVISITED_LAND:
            neighbors.append(Cell(i + 1, j))
        if j > 0 and grid[i][j - 1] == GroundType.UNVISITED_LAND:
            neighbors.append(Cell(i, j - 1))
        if j < len(grid[0]) - 1 and grid[i][j + 1] == GroundType.UNVISITED_LAND:
            neighbors.append(Cell(i, j + 1))
        return neighbors