from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        @cache
        def try_rob(i: int) -> int:
            if i >= len(nums):
                return 0
            # we need to try robbing this house, increment 2 because we can't rob the neighbor
            rob_this_house = nums[i] + try_rob(i + 2)
            # and we need to try not robbing this house
            skip_this_house = try_rob(i + 1)
            # we can return the better of our 2 choices
            return max(rob_this_house, skip_this_house)
        return try_rob(0)
        