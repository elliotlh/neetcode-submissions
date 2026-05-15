from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def topDown(i: int, j: int) -> int:
            if i >= len(text1) or j >= len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + topDown(i + 1, j + 1)
            return max(
                topDown(i + 1, j),
                topDown(i, j + 1),
            )
        return topDown(0, 0)
        