class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_fruits = 0
        rotting_fruit_queue = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_fruits += 1
                elif grid[i][j] == 2:
                    rotting_fruit_queue.append((i, j))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        minutes = 0
        while rotting_fruit_queue:
            minutes += 1
            moves_in_minute = len(rotting_fruit_queue)
            for _ in range(moves_in_minute):
                i, j = rotting_fruit_queue.popleft()
                for i_offset, j_offset in directions:
                    new_i, new_j = i + i_offset, j + j_offset
                    if not self.isInBounds(grid, new_i, new_j):
                        continue
                    if grid[new_i][new_j] == 1:
                        fresh_fruits -= 1
                        grid[new_i][new_j] = 2
                        rotting_fruit_queue.append((new_i, new_j))
        return max(minutes - 1, 0) if fresh_fruits == 0 else -1

            
    def isInBounds(self, grid: List[List[int]], i: int, j: int) -> bool:
        if i < 0 or i >= len(grid):
            return False
        if j < 0 or j >= len(grid[0]):
            return False
        return True
        