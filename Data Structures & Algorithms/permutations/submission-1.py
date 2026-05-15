class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        candidate_set = set(nums)
        def generatePermutations(remaining_set: Set[int], current_permutation: List[int]):
            if len(remaining_set) == 0:
                permutations.append(current_permutation.copy())
                return
            for num in remaining_set:
                current_permutation.append(num)
                generatePermutations(remaining_set - {num}, current_permutation)
                current_permutation.pop()
        generatePermutations(candidate_set, [])
        return permutations
            
        