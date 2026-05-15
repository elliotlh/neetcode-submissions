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
        def doPartition(i: int, curr: int):
            nonlocal can_partition
            if i >= len(nums):
                return
            if can_partition:
                return
            if total - curr == curr:
                can_partition = True
                return
            # for every element, I can either include it or not include it in my subset
            doPartition(i + 1, curr + nums[i])
            doPartition(i + 1, curr)

        doPartition(0, 0)

        return can_partition