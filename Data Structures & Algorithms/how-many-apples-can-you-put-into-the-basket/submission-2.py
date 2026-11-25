class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        total = 0
        for i in range(len(weight)):
            if total + weight[i] <= 5000:
                total += weight[i]
            else:
                return i
        return len(weight)
