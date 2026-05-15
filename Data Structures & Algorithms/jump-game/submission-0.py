class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # [1,20,22,0]
        furthest_reachable_idx = nums[0]
        for idx, num in enumerate(nums):
            if idx > furthest_reachable_idx:
                return False
            furthest_reachable_idx = max(furthest_reachable_idx, idx + num)
            print(furthest_reachable_idx, idx)
            
            if furthest_reachable_idx >= len(nums) - 1:
                return True
        return furthest_reachable_idx >= len(nums) - 1