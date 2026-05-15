from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def calculateMaxProfit(buy_mode: bool, i: int) -> int:
            if i >= len(prices):
                return 0
            if buy_mode:
                # in buy mode we can either skip this choice or buy it
                return max(
                    -prices[i] + calculateMaxProfit(not buy_mode, i + 1),
                    calculateMaxProfit(buy_mode, i + 1)
                )
            else:
                # in sell mode, we can either skip this sell or sell and take the cooldown
                return max(
                    prices[i] + calculateMaxProfit(not buy_mode, i + 2),
                    calculateMaxProfit(buy_mode, i + 1)
                )
        return max(calculateMaxProfit(True, 0), 0)
        