class Solution:
    def jump(self, nums: List[int]) -> int:
        left, right = 0, 0
        jumps = 0
        while right < len(nums) - 1:
            farthest_point = right
            for i in range(left, right + 1):
                farthest_point = max(farthest_point, i + nums[i])
            jumps += 1
            left = right + 1
            right = farthest_point
        return jumps