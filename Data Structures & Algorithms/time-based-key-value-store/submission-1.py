from dataclasses import dataclass


@dataclass
class TimeValue:
    value: str
    time: int

class TimeMap:
    def __init__(self):
        self.time_map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append(TimeValue(value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        options = self.time_map[key]
        if len(options) == 0:
            return ''
        lo, hi = 0, len(options) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if options[mid].time == timestamp:
                return options[mid].value
            elif timestamp < options[mid].time:
                hi = mid - 1
            else:
                lo = mid + 1
        return options[lo - 1].value if lo > 0 else ''
        
