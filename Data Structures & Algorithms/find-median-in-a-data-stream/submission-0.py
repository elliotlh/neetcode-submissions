class HeapManager:
    def __init__(self):
        self.max_heap_lower = []
        self.min_heap_higher = []

    def push(self, val: int) -> None:
        if not self.max_heap_lower:
            heapq.heappush(self.max_heap_lower, -val)
            return
        # This value is small and goes on my small side
        if val < -self.max_heap_lower[0]:
            heapq.heappush(self.max_heap_lower, -val)
        else:
            # This value is big and goes on my big side
            heapq.heappush(self.min_heap_higher, val)
        self._balance()

    def pop_min(self) -> int:
        returned = heapq.heappop(self.min_heap_higher)
        return returned

    def pop_max(self) -> int:
        returned = -heapq.heappop(self.max_heap_lower)
        return returned

    def _balance(self) -> None:
        while len(self.max_heap_lower) > len(self.min_heap_higher) + 1:
            heapq.heappush(self.min_heap_higher, self.pop_max())
        while len(self.max_heap_lower) + 1 < len(self.min_heap_higher):
            heapq.heappush(self.max_heap_lower, -self.pop_min())

class MedianFinder:

    def __init__(self):
        self.heap_manager = HeapManager()

    def addNum(self, num: int) -> None:
        self.heap_manager.push(num)

    def findMedian(self) -> float:
        if len(self.heap_manager.max_heap_lower) == len(self.heap_manager.min_heap_higher):
            total = -self.heap_manager.max_heap_lower[0] + self.heap_manager.min_heap_higher[0]
            return total / 2.0
        elif len(self.heap_manager.max_heap_lower) > len(self.heap_manager.min_heap_higher):
            return -self.heap_manager.max_heap_lower[0]
        else:
            return self.heap_manager.min_heap_higher[0]
        
        