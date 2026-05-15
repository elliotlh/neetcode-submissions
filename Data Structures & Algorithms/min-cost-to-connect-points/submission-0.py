from _heapq import heappush
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                p1, p2 = points[i], points[j]
                manhattan = self.getManhattanDistance(p1, p2)
                graph[(p1[0], p1[1])].append((p2, manhattan))
        
        min_heap = [(0, points[0])]
        visited = set()
        total_cost = 0
        while min_heap:
            cost, to_point = heapq.heappop(min_heap)
            
            if (to_point[0], to_point[1]) in visited:
                continue
            visited.add((to_point[0], to_point[1]))
            total_cost += cost
            for point, cost in graph[(to_point[0], to_point[1])]:
                heappush(min_heap, (cost, point))
        return total_cost
    
    def getManhattanDistance(self, p1: List[int], p2: List[int]) -> int:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])