from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)
        @cache
        def dfs(i: int, end: int) -> int:
            if i >= end:
                return 0
            # I can steal from this house
            choose_to_steal = nums[i] + dfs(i + 2, end)
            choose_to_pass = dfs(i + 1, end)
            return max(choose_to_pass, choose_to_steal)
        return max(dfs(0, len(nums) - 1), dfs(1, len(nums)))

        