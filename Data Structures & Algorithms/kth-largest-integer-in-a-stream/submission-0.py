class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        return self.pop_and_return()

    def pop_and_return(self) -> int:
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        
