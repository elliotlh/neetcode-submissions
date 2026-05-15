from typing import Tuple
from functools import cache

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        for each character in s
            if s[i] == t[0]
                do_search

        do_search:
            recursive backtracking function that takes in an index and a candidate length
            if candidate length == len(t), then we have a valid candidate and we can return out
            otherwise, we need to process the rest of the string starting from supplied index

        """

        @cache
        def search(s_index: int, candidate_length: int) -> int:
            if len(t) == candidate_length:
                return 1
            total_search_results = 0
            for j in range(s_index, len(s)):
                if s[j] == t[candidate_length]:
                    total_search_results += search(j + 1, candidate_length + 1)
            return total_search_results

        total = 0
        for i in range(len(s)):
            if s[i] == t[0]:
                total += search(i + 1, 1)
        return total