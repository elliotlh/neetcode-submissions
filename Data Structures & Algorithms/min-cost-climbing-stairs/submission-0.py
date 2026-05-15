from functools import cache
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def climbStairsWithChoice(i: int) -> int:
            if i >= len(cost):
                return 0
            step_cost = cost[i]
            one_step_cost = climbStairsWithChoice(i + 1)
            two_step_cost = climbStairsWithChoice(i + 2)
            return min(
                step_cost + one_step_cost,
                step_cost + two_step_cost,
            )
        return min(climbStairsWithChoice(0), climbStairsWithChoice(1))