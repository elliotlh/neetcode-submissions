class Solution:
    def stringify(self, subset: List[int]) -> str:
        return ''.join([str(x) for x in subset])

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets: List[List[int]] = []
        seen: Set[str] = set()

        def getSubsets(i: int, current_subset: List[int]) -> None:
            nonlocal subsets
            if i == len(nums):
                stringed = self.stringify(current_subset)
                if stringed not in seen:
                    subsets.append(current_subset.copy())
                    seen.add(stringed)
                return
            for j in range(i, len(nums)):
                current_subset.append(nums[i])
                getSubsets(j + 1, current_subset)
                current_subset.pop()
        
        current_num = nums[0]
        for i in range(len(nums)):
            getSubsets(i, [])
                
        subsets.append([])
        return subsets
        