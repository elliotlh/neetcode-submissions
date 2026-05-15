class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results: List[List[int]] = []
        def generateSubsets(i: int, current_subset: List[int]) -> None:
            if i > len(nums):
                return
            if i == len(nums):
                results.append(current_subset.copy())
                return
            # For each element, consider skipping it
            generateSubsets(i + 1, current_subset)
            # Or consider adding it
            current_subset.append(nums[i])
            generateSubsets(i + 1, current_subset)
            current_subset.pop()
        generateSubsets(0, [])
        return results

        