class Solution:

    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        def reverse(arr, l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1


        if k == 0:
            return grid
        flattened = [item for row in grid for item in row]
        k %= len(flattened)
        if k == 0:
            return grid
        reverse(flattened, 0, len(flattened) - 1)
        reverse(flattened, 0, k - 1)
        reverse(flattened, k, len(flattened) - 1)
        c = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = flattened[c]
                c += 1
        
        return grid
