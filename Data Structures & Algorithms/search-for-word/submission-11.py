from typing import Tuple
from functools import cache

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        visited: Set[Tuple[int, int]] = set()
        
        def dfs(i: int, j: int, remaining_word: str) -> bool:
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            coord = (i, j)
            if coord in visited:
                return False
            if remaining_word[0] != board[i][j]:
                return False
            visited.add(coord)
            if len(remaining_word) == 1:
                visited.discard(coord)
                return remaining_word[0] == board[i][j]
            remaining = remaining_word[1:]
            if dfs(i - 1, j, remaining):
                return True
            if dfs(i + 1, j, remaining):
                return True
            if dfs(i, j - 1, remaining):
                return True
            if dfs(i, j + 1, remaining):
                return True
            visited.discard(coord)
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, word):
                        return True
                    else:
                        visited = set()
        return False
        