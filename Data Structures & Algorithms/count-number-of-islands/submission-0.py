class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        1. Traverse the entire grid, 
            When we see a 1, increment our island counter and then do a DFS
        2. DFS should explore out from a point, and mark any 1's found as 0s,
        """

        def dfs(i: int, j: int) -> None:
            if i < 0 or i >= len(grid):
                return
            if j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    island_count += 1
                    dfs(i, j)
        return island_count
        
        