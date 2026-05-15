class Solution:
    def canEatPilesAtSpeed(self, piles: List[int], h: int, k: int) -> bool:
        for p in piles:
            h -= math.ceil(p / k)
            if h < 0:
                # We ran out of time, we need to up our pace
                return False
        # We ate all the bananas fast enough
        return True
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper_bound = max(piles)
        lo, hi = 1, upper_bound
        minimum = upper_bound
        while lo <= hi:
            k = (lo + hi) // 2
            if self.canEatPilesAtSpeed(piles, h, k):
                minimum = min(minimum, k)
                hi = k - 1
            else:
                lo = k + 1
        return minimum
            
        