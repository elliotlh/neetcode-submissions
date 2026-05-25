from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        we could solve this with dp. we cant just greedily take the largest
        coin because imagine this scenario [12,5,1] where are amount = 15
        we'd get 12 + 1 + 1 + 1 vs 5 + 5 + 5

        For DP, it is common to model it as a recursive decision tree (top down)
        So we need to figure out how we make decisions

        If we sort the coins, we can:
        # Either choose to include this denomination and recurse
        # Skip this denomination and move onto the next one
        # We could model this w/ 2 state variables, or just keep
        # track of amount, which is what we'll do
        """
        if amount == 0:
            return 0
        coins.sort(reverse=True)
        @cache
        def distributeCoins(remaining_coins: int):
            if remaining_coins == 0:
                return 0

            # for our remaining amount, our choices are any denomination <= remaining_coins
            # This doubles as our base case, if there are no matches, then we are out of luck
            coins_required = float('inf')
            for coin in coins:
                if coin <= remaining_coins:
                    use_denomination = 1 + distributeCoins(remaining_coins - coin)
                    coins_required = min(use_denomination, coins_required)
            return coins_required
        res = distributeCoins(amount)
        return -1 if math.isinf(res) else res