from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        @cache
        def makeChoices(i: int, holding: bool) -> int:
            if i >= len(prices):
                return 0
            # For each stage, I can make some choices
            # if I'm holding, I can sell and claim the profit
            profit = 0
            if holding:
                profit = prices[i] + makeChoices(i + 1, not holding)
            else:
                profit = -prices[i] + makeChoices(i + 1, not holding)
            do_nothing = makeChoices(i + 1, holding)
            return max(profit, do_nothing)
        return makeChoices(0, False)
            
        