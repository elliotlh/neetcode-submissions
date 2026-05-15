class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        def binSearch(start: int) -> int:
            lo, hi = start + 1, len(numbers) - 1
            need = target - numbers[start]
            if need < numbers[lo]:
                return -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if numbers[mid] == need:
                    return mid
                elif numbers[mid] < need:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return -1
        for i in range(len(numbers)):
            got = binSearch(i)
            if got != -1:
                return [i + 1, got + 1]
        return []
        