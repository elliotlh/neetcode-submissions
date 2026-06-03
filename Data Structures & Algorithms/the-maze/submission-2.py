from dataclasses import dataclass
from typing import Tuple
directions = {
    'N': (-1, 0),
    'S': (1, 0),
    'E': (0, 1),
    'W': (0, -1),
}

@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def apply_offset(self, offset: Tuple[int, int]) -> 'Point':
        return Point(self.x + offset[0], self.y + offset[1])

    def get_neighbors(self) -> Dict[str, 'Point']:
        res = {}
        for d, offset in directions.items():
            res[d] = self.apply_offset(offset)
        return res

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        s = Point(start[0], start[1])
        dest = Point(destination[0], destination[1])

        def is_in_bounds(n: Point) -> bool:
            if not (n.x >= 0 and n.x < len(maze) and n.y >= 0 and n.y < len(maze[0])):
                return False
            return maze[n.x][n.y] == 0

        def get_inbound_neighbors(p: Point) -> Dict[str, Point]:
            neighbors = p.get_neighbors()
            res = {}
            for d, p in neighbors.items():
                if is_in_bounds(p):
                    res[d] = p
            return res

        visited: Set[Point] = set()

        def travel_until_choice(curr: Point, direction: str):
            adjusted = curr.apply_offset(directions[direction])
            while is_in_bounds(adjusted):
                curr = adjusted
                adjusted = curr.apply_offset(directions[direction])
            return curr

        def DFS(curr: Point) -> bool:
            if curr in visited:
                return False
            if curr == dest:
                return True
            visited.add(curr)
            for d, n in get_inbound_neighbors(curr).items():
                new_n = travel_until_choice(n, d)
                if DFS(new_n):
                    return True
            return False
        return DFS(s)     
        