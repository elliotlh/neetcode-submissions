class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_subarray = 0
        best = nums[0]
        for num in nums:
            if current_subarray < 0:
                current_subarray = num
            else:
                current_subarray += num
            best = max(best, current_subarray)
        return best