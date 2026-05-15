class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[mid][0] == target:
                return True
            # if my target is smaller than this element, its definitely in a previous row
            elif matrix[mid][0] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        row = lo - 1 if lo > 0 else 0
        lo, hi = 0, len(matrix[0]) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return False