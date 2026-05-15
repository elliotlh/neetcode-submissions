from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def traverse(i: int, current_sum: int) -> int:
            # base case 1: we went too far -- safety check
            if i >= len(nums):
                return 0
            # case 2: we are on our last element
            if i == len(nums) - 1:
                num_ways = 0
                # when considering the last element, there are up to 2 options
                # that contribute to the overall total. 
                if current_sum + nums[i] == target:
                    num_ways += 1
                if current_sum - nums[i] == target:
                    num_ways += 1
                return num_ways

            return traverse(i + 1, current_sum + nums[i]) + traverse(i + 1, current_sum - nums[i])

        return traverse(0,0)