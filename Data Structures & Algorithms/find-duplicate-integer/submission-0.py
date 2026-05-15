class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen: Set[int] = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        raise ValueError('should have found an answer')