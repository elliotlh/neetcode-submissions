from enum import IntEnum
from dataclasses import dataclass
from typing import Self, Optional, Tuple

class Direction(IntEnum):
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    UP = 4

@dataclass(frozen=True)
class Point:
    i: int
    j: int

    def get_next_point(self, d: Direction) -> 'Point':
        if d == Direction.UP:
            return Point(self.i - 1, self.j)
        if d == Direction.DOWN:
            return Point(self.i + 1, self.j)
        if d == Direction.LEFT:
            return Point(self.i, self.j - 1)
        if d == Direction.RIGHT:
            return Point(self.i, self.j + 1)
        raise ValueError("Unexpected direction")

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        next_direction: Dict[Direction, Direction] = {
            Direction.RIGHT: Direction.DOWN,
            Direction.DOWN: Direction.LEFT,
            Direction.LEFT: Direction.UP,
            Direction.UP: Direction.RIGHT
        }
        current_direction = Direction.RIGHT
        current_point = Point(0, 0)
        visited: Set[Point] = set([current_point])

        def isValidPoint(p: Point) -> bool:
            if p.i < 0 or p.i >= len(matrix):
                return False
            if p.j < 0 or p.j >= len(matrix[0]):
                return False
            return p not in visited

        def getNextPoint(p: Point, d: Direction) -> Tuple[Optional[Point], Optional[Direction]]:
            next_point = p.get_next_point(d)
            if isValidPoint(next_point):
                visited.add(next_point)
                return next_point, d
            next_point = p.get_next_point(next_direction[d])
            if isValidPoint(next_point):
                visited.add(next_point)
                return next_point, next_direction[d]
            return None, None
        
        n = len(matrix)
        m = len(matrix[0])
        out: List[int] = []
        for i in range(n * m):
            out.append(matrix[current_point.i][current_point.j])
            current_point, current_direction = getNextPoint(current_point, current_direction)
            if not current_point or not current_direction:
                break
        return out

            



        
        