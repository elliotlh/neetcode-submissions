class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_sum: List[int] = [0] * len(nums)
        prefix_sum[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1] * nums[i]
        
        suffix_sum: List[int] = [0] * len(nums)
        suffix_sum[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] * nums[i]
        
        output: List[int] = [0] * len(nums)
        for i in range(len(output)):
            left = 1 if i == 0 else prefix_sum[i - 1]
            right = 1 if i == len(output) - 1 else suffix_sum[i + 1]
            output[i] = left * right
        
        return output
        