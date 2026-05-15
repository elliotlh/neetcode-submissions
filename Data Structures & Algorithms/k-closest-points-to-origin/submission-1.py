class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for point in points:
            distance = self.calculateEuclidianDistanceFromOrigin(point)
            # if this is a closer candidate, kick the biggest candidate and replace with better option
            # since this is python, we have to negate, so the more negative distance is the "bigger" istance
            if len(max_heap) == k:
                if -distance > max_heap[0][0]:
                    heapq.heapreplace(max_heap, (-distance, point))
            else:
                heapq.heappush(max_heap, (-distance, point))
        return [point for _, point in max_heap]

    def calculateEuclidianDistanceFromOrigin(self, point: List[int]) -> float:
        x1, y1 = point
        return math.sqrt((x1**2) + (y1**2))