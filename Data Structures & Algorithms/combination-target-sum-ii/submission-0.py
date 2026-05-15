class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        def generateCombinationSums(i: int, res: List[int]):

            total = sum(res)
            if total > target:
                return
            if total == target:
                results.append(res[:])
                return
            if i >= len(candidates):
                return
            # choice 1: include current number
            res.append(candidates[i])
            generateCombinationSums(i + 1, res)
            res.pop()
            # choice 2: skip current number (or any variant)
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            generateCombinationSums(i + 1, res)
        generateCombinationSums(0, [])
            
        return results
        