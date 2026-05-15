class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0
        while left < right:
            bounding_height = min(heights[left], heights[right])
            max_area = max(max_area, bounding_height * (right - left))
            if heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
        return max_area
        