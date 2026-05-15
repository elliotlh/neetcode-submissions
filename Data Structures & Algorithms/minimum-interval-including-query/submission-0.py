class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        1. We sort the intervals
        2. For each query, we perform 2 binary searches. We get a candidate set 
        """
        intervals.sort(key=lambda x: (x[0], x[1]))
        out: List[int] = []
        for query in queries:
            delta = float('inf')
            for interval in intervals:
                if query >= interval[0] and query <= interval[1] and (interval[1] - interval[0] + 1) < delta:
                    delta = interval[1] - interval[0] + 1
            out.append(int(delta) if not math.isinf(delta) else -1)

        return out
        