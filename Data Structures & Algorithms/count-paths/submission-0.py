from functools import cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        @cache
        def traverse(i: int, j: int) -> int:
            # base case 1: we went out of bounds
            if i >= m or j >= n:
                return 0
            # base case 2: we made it, this must be a valid path
            if i == m - 1 and j == n - 1:
                return 1
            return traverse(i + 1, j) + traverse(i, j + 1)
        return traverse(0,0)
        

        