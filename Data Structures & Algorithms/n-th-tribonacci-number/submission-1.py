class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1
        dp = [1, 1, 0]
        for i in range(2, n - 1):
            dp[i % 3] = sum(dp)
        return sum(dp)
        




        