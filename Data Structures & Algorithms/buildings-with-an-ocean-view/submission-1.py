class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        if len(heights) == 0:
            return []
        if len(heights) == 1:
            return [0]

        postfix = [0] * len(heights)
        for i in range(len(heights) - 2, -1, -1):
            postfix[i] = max(heights[i + 1], postfix[i + 1])
        out = []
        for i, height in enumerate(heights):
            if height > postfix[i]:
                out.append(i)
        return out
        
        