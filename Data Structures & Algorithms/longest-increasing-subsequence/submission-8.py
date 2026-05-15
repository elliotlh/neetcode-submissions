from functools import cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        import sys
        sys.setrecursionlimit(2000)
        """
        [1,1,2,2,3,3,4]
        """
        @cache
        def findLIS(i: int, last_element: int) -> int:
            if i >= len(nums):
                return 0
            # Choice 1: choose this element
            include = 0
            if nums[i] > last_element:
                include = 1 + findLIS(i + 1, nums[i])
            
            # Choice 2: skip this element
            skip = findLIS(i + 1, last_element)
            return max(include, skip)
        return findLIS(0, -1001)