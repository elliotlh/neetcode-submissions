class Solution:
    def trap(self, height: List[int]) -> int:
        """
        prefix_sum: [0,2,2,3,3,3,3,3,3,3]
                    [0,2,0,3,1,0,1,3,2,1]
        suffix_sum: [3,3,3,3,3,3,3,3,2,1]
        """
        prefix_sum = [0] * len(height)
        prefix_sum[0] = height[0]
        suffix_sum = [0] * len(height)
        suffix_sum[-1] = height[-1]
        for i in range(1, len(height)):
            j = len(height) - 1 - i
            prefix_sum[i] = max(prefix_sum[i - 1], height[i])
            suffix_sum[j] = max(suffix_sum[j + 1], height[j])
        
        total_trapped = 0
        for i in range(1, len(height) - 1):
            neighbors = min(prefix_sum[i - 1], suffix_sum[i + 1])
            delta = neighbors - height[i]
            if delta > 0:
                total_trapped += delta
        return total_trapped
        