from typing import Tuple
class Solution:
    def expand(self, s: str) -> List[str]:
        results: List[str] = []
        def backtrack(i: int, curr: str):
            if i > len(s):
                return
            if i == len(s):
                results.append(curr)
                return
            for j in range(i, len(s)):
                if s[j] != '{':
                    curr += s[j]
                else:
                    options, next = self.getBraceOptions(s, j)
                    for option in options:
                        backtrack(next, curr + option)
                    return
            results.append(curr)
        backtrack(0, '')
        return results


    def getBraceOptions(self, s: str, i: int) -> Tuple[List[str], int]:
        closing_index = s.index('}', i)
        return s[i+1:closing_index].split(','), closing_index + 1
        