from dataclasses import dataclass
from typing import Self

@dataclass(frozen=True)
class Point:
    x: int
    y: int

    @classmethod
    def from_raw_point(cls, raw_point: List[int]) -> Self:
        x, y = raw_point[0], raw_point[1]
        return cls(x, y)

    def upper_diagonal(self) -> int:
        return self.x - self.y

    def lower_diagonal(self) -> int:
        return self.x + self.y

class CountSquares:

    def __init__(self):
        # Bug 1 fix: two separate dicts so upper/lower never contaminate each other
        self.upper_diagonals: Dict[int, List[Point]] = collections.defaultdict(list)
        self.lower_diagonals: Dict[int, List[Point]] = collections.defaultdict(list)
        self.points: Dict[Point, int] = collections.defaultdict(int)

    def add(self, point: List[int]) -> None:
        p = Point.from_raw_point(point)
        self.points[p] += 1
        # Only add to diagonal lists once — self.points[p] handles duplicates
        if self.points[p] == 1:
            self.upper_diagonals[p.upper_diagonal()].append(p)
            self.lower_diagonals[p.lower_diagonal()].append(p)

    def check_square_from_points(self, a: Point, b: Point) -> int:
        if a == b:
            return 0
        compliments = [Point(a.x, b.y), Point(b.x, a.y)]
        for compliment in compliments:
            if compliment not in self.points:
                return 0
        # Bug 2 fix: multiply instead of add
        # Bug 3 fix: include self.points[b] as a factor
        return self.points[b] * self.points[compliments[0]] * self.points[compliments[1]]

    def count(self, point: List[int]) -> int:
        p = Point.from_raw_point(point)
        total = 0

        for upper_diagonal in self.upper_diagonals[p.upper_diagonal()]:
            total += self.check_square_from_points(p, upper_diagonal)
        for lower_diagonal in self.lower_diagonals[p.lower_diagonal()]:
            total += self.check_square_from_points(p, lower_diagonal)
        return total