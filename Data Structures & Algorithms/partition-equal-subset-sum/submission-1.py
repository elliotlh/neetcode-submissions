from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        return self.partition(nums, total)

    def partition(self, nums: List[int], total: int) -> bool:
        can_partition: bool = False
        @cache
        def doPartition(i: int, curr: int) -> bool:
            nonlocal can_partition
            if i >= len(nums):
                return False
            if total - curr == curr:
                return True
            # for every element, I can either include it or not include it in my subset
            return (
                doPartition(i + 1, curr + nums[i]) or
                doPartition(i + 1, curr)
            )

        return doPartition(0, 0)