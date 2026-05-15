class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
          '' m o n k e y s
        '' 0 1 2 3 4 5 6 7
        m  1 0 1 2 3 4 5 6
        o  2 1 0 2 3 4 5 6
        n  3 2 1 0 1 2 3 4
        e  4 3 2 1 1 1 2 3
        y  5 4 3 2 1 1 1 2
        """
        grid = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]
        for i in range(len(grid)):
            grid[i][0] = i
        for j in range(len(grid[0])):
            grid[0][j] = j
        
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                match = 0 if word1[j - 1] == word2[i - 1] else 1
                grid[i][j] = min(
                    1 + grid[i - 1][j],
                    1 + grid[i][j - 1],
                    match + grid[i - 1][j - 1],
                )

        return grid[-1][-1]
        