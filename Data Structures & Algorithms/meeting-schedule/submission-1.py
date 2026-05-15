"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        1. We want to sort all intervals by their start time so we can compare potentially conflicting meetings
        2. If any meeting ends after the next meeting has begun, then we can't fit it on the calendar
        3. Otherwise, we can totally return happily
        """
        intervals.sort(key=lambda x: x.start)
        for i in range(len(intervals) - 1):
            interval = intervals[i]
            # important check, if our meeting ends after the next meeting starts
            # that is our return criteria. This always works because we sorted by start time
            if interval.end > intervals[i + 1].start:
                return False
            
        return True

