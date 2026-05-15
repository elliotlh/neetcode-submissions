from typing import Tuple
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def isInBounds(i: int, j: int) -> bool:
            if i < 0 or i >= len(heights):
                return False
            if j < 0 or j >= len(heights[0]):
                return False
            return True

        def getReachable(i: int, j: int, can_reach: Set[Tuple[int, int]]):
            if (i, j) in can_reach:
                return False
            can_reach.add((i, j))
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for d in directions:
                di, dj = i + d[0], j + d[1]
                if not isInBounds(di, dj):
                    continue
                if heights[i][j] <= heights[di][dj]:
                    getReachable(di, dj, can_reach)
        pacific = set()
        for j in range(len(heights[0])):
            getReachable(0, j, pacific)
        for i in range(len(heights)):
            getReachable(i, 0, pacific)
        
        atlantic = set()
        for j in range(len(heights[0])):
            getReachable(len(heights) - 1, j, atlantic)
        for i in range(len(heights)):
            getReachable(i, len(heights[0]) - 1, atlantic)
        return list(atlantic & pacific)
