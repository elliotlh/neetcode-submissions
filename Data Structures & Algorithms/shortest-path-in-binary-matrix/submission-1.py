from typing import Tuple
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        n = len(grid)
        visited: Set[Tuple[int, int]] = set([(0, 0)])
        queue = collections.deque([(0, 0)])

        def is_in_bounds(coord: Tuple[int, int]) -> bool:
            x, y = coord
            if x < 0 or x >= n:
                return False
            if y < 0 or y >= n:
                return False
            return grid[x][y] == 0

        def get_unvisited_neighbors(x: int, y: int) -> List[Tuple[int, int]]:
            neighbors = []
            for i in range(-1, 2):
                for j in range(-1, 2):
                    coord = (x + i, y + j)
                    if is_in_bounds(coord) and coord not in visited:
                        neighbors.append(coord)
                        visited.add(coord)
            return neighbors
            
        total_levels = 0
        while queue:
            level_size = len(queue)
            total_levels += 1
            for _ in range(level_size):
                coord = queue.popleft()
                x, y = coord
                if coord[0] == n - 1 and coord[1] == n - 1:
                    return total_levels
                queue.extend(get_unvisited_neighbors(x, y))
                

        return -1
        