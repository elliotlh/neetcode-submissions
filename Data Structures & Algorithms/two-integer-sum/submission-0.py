class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed = {}
        for i, num in enumerate(nums):
            if num in needed:
                return [needed[num], i]
            needed[target - num] = i
            
        raise Exception('not expected')

        