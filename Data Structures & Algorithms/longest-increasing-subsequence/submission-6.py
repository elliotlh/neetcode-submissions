from functools import cache
import sys
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sys.setrecursionlimit(10**6)
        """
        [1,1,2,2,3,3,4]
        """
        @cache
        def findLIS(i: int, j: int) -> int:
            if i >= len(nums):
                return 0
            # Choice 1: choose this element
            include = 0
            if j == -1 or nums[i] > nums[j]:
                include = 1 + findLIS(i + 1, i)
            
            # Choice 2: skip this element
            skip = findLIS(i + 1, j)
            return max(include, skip)
        return findLIS(0, -1)
                
            
            