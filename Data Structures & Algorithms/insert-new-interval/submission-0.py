class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Bisect left to get insertion point
        lo, hi = 0, len(intervals) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            # if my candidate ends before my new interval starts
            if intervals[mid][0] < newInterval[0]:
                lo = mid + 1
            else:
                hi = mid - 1
        intervals.insert(lo, newInterval)
        res: List[List[int]] = []
        for interval in intervals:
            # If I have nothing or my current interval ends before my candidate interval starts
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res
        