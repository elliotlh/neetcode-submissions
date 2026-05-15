"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        0. 1. 2. 3. 4. 5. 6. 7. 8. 9. 
        |--|--|--|--|--|--|--|--|--|--
        |.    |
           |.       |
              |.          |
                    |.       |
                       |.       |
        (0,40)
        (5,10)
        (10,20)

        (5,9)(8,13)(9,20)(0,40)
             (9,13)
                   
        (0,40)(5,10)(10,15)(11,16)(45,50)
        """
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x: (x.start, x.end))
        end_time = [intervals[0].end]
        num_rooms = 1   
        for i in range(1, len(intervals)):
            interval = intervals[i]
            while end_time and end_time[0] <= interval.start:
                heapq.heappop(end_time)
            heapq.heappush(end_time, interval.end)
            num_rooms = max(num_rooms, len(end_time))
        return num_rooms



        