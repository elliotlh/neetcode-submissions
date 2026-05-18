class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        cloned = arr.copy()
        requires_adjustment = True
        while requires_adjustment:
            requires_adjustment = False
            for i in range(1, len(arr) - 1):
                if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                    requires_adjustment = True
                    cloned[i] += 1
                if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                    requires_adjustment = True
                    cloned[i] -= 1
            if requires_adjustment:
                arr = cloned.copy()
        return cloned
        