from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @cache
        def findWordBreaks(s: str, i: int) -> bool:
            if i >= len(s):
                return True
            for j in range(i, len(s)):
                word = s[i:j+1]
                for candidate in wordDict:
                    if word == candidate and findWordBreaks(s, j + 1):
                        return True
            return False
        return findWordBreaks(s, 0)
        