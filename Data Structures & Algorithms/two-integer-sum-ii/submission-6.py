class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            calculated = numbers[l] + numbers[r]
            if calculated == target:
                return [l + 1, r + 1]
            elif calculated > target:
                r -= 1
            else:
                l += 1
        return [-1, -1]
            