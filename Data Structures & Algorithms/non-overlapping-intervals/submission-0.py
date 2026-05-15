class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        [1,10],[2,4],[2,6]
        """
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x: (x[0], x[1]))
        intervals_to_delete = 0
        merge_candidate = intervals[0]
        for i in range(1, len(intervals)):
            if merge_candidate[1] > intervals[i][0]:
                merge_candidate[1] = min(merge_candidate[1], intervals[i][1])
                intervals_to_delete += 1
            else:
                merge_candidate = intervals[i]
        return intervals_to_delete
        