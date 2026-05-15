class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        check if array has rotated
        if not, return [0]
        otherwise, binary search for pivot point
        which is also the minimum/maximum
        """

        # base cases
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]

        # otherwise binary search pivot point
        lo, hi = 1, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            # if i'm smaller than the element to my left, i'm the pivot point
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            # if I'm bigger than minimum, pivot point must be to my right
            elif nums[mid] > nums[0]:
                lo = mid + 1
            # otherwise i'm in the small side of the search space, but not the minimum
            else:
                hi = mid - 1
        # unexpected, should always find pivot
        return -1            
        