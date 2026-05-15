"""
                (0, 4)
            (0, 1) (1, 2).  (2,0
        (0, 0).      (2, 0)
        
"""
from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        This feels like dynamic programming because I think there is a recurrence relation
        Our idea will basically be recursive backtracking solution where we have 2 choices
        1. Take the coin (if possible)
        2. Skip the coin and move to the next smallest denomination

        When we get to 0 for our remaining amount, thats a valid way to reach our target
        state. We increment our counter and try all possible routes to get there
        """
        coins.sort(reverse=True)
        @cache
        def backtrack(i: int, remaining: int) -> int:
            # case 1: happy path, we literally can't do anything else on this path
            if remaining == 0:
                return 1
            # case 2: there are no remaining choices
            if remaining < 0 or i >= len(coins):
                return 0
            
            # Our goal is to get the total choices
            take_coin = 0
            # Choice 1
            if remaining >= coins[i]:
                take_coin = backtrack(i, remaining - coins[i])
            
            # Choice 2
            skip_coin = backtrack(i + 1, remaining)
            
            return take_coin + skip_coin
        return backtrack(0, amount)
        