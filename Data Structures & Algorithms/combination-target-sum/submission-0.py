class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        """
        This is a classic backtracking solution
        At any given number, we have the choice:
            - include this number 
            - skip this number

        If we skip, we increase the index, if we include, we don't increase the index
        but we increase the target
        """
        def computeCombinations(i: int, total: int, curr_set: List[int]):
            # Base case 1: check our append condition
            if total > target:
                return
            if total == target:
                results.append(curr_set.copy())
                return
            # Then check our boundary before re-entering the recursion
            if i >= len(nums):
                return

            # choice 1: include number
            curr_set.append(nums[i])
            computeCombinations(i, total + nums[i], curr_set)
            curr_set.pop()

            # choice 2: ignore number and try the next one
            computeCombinations(i + 1, total, curr_set)
        computeCombinations(0, 0, [])
        return results