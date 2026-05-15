class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        1. We want to check if the array is actually pivoted
        2. We want to find the pivot point using binary search (e.g. if nums[mid] < nums[mid + 1])
        3. Check which side of the search space our target is at
        4. Binary search that half of the search space for our target
        """
        # 1a. safety checks
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        lo, hi = 0, len(nums) - 1
        if nums[0] == target:
            return 0
        if nums[-1] == target:
            return len(nums) - 1
        if nums[0] > nums[-1]:
            pivot = self.binSearchPivot(nums)
            if target > nums[0]:
                return self.binSearchTarget(nums, target, lo, pivot)
            else:
                return self.binSearchTarget(nums, target, pivot + 1, hi)
        return self.binSearchTarget(nums, target, lo, hi)


    def binSearchTarget(self, nums: List[int], target: int, lo: int, hi: int) -> int:
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1
        
    def binSearchPivot(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[mid + 1]:
                return mid
            # Otherwise if im in sorted order, then the pivot must be further along
            elif nums[mid] > nums[0]:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

        