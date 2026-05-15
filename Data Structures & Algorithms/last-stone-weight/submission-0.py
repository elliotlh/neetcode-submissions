class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            stone_a = heapq.heappop(max_heap)
            stone_b = heapq.heappop(max_heap)
            # this logic is inverted because python has no max heap
            delta = abs(stone_a - stone_b)
            if delta != 0:
                heapq.heappush(max_heap, -delta)
        return -max_heap[0] if len(max_heap) == 1 else 0



        