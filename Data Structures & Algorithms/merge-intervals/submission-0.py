class Solution:
    def intervalOverlaps(self, a: List[int], b: List[int]) -> bool:
        return a[1] >= b[0]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        1. Sort intervals by x[0], secondary sort on x[1]
        2. Iterate over intervals,
                if a[1] >= b[0]
                    merge by setting a[1] = max(a[1], b[1])
                else:
                    append current interval to result set
        3. Case 1:
                Our last interval is part of the merge. We are done
            Case 2:
                Out last interval was NOT part of the merge, we need to add it
                to the result set
        4. Return result set
        """
        if len(intervals) < 2:
            return intervals
        intervals.sort(key=lambda x: (x[0], x[1]))
        result: List[List[int]] = []
        current_interval = intervals[0]
        last_append_idx = -1
        for i in range(1, len(intervals)):
            if self.intervalOverlaps(current_interval, intervals[i]):
                current_interval[1] = max(current_interval[1], intervals[i][1])
            else:
                result.append(current_interval)
                last_append_idx = i - 1
                current_interval = intervals[i]
        if last_append_idx != len(intervals) - 1:
            result.append(current_interval)
        return result



        