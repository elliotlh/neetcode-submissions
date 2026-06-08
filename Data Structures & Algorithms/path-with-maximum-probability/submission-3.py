from typing import Tuple
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        """
        This is a dijkstra problem
        This can be modeled as a graph where edge weights are probabilities

        Dijkstras is a frontier algorithm where we greedily extract items from the heap
        For our case, our heap will track the cost as the negated probability
        """
        # Create the graph in a more concise format
        graph: Dict[int, List[Tuple[int, float]]] = collections.defaultdict(list)
        for i, (from_node, to_node) in enumerate(edges):
            graph[from_node].append((to_node, succProb[i]))
            graph[to_node].append((from_node, succProb[i]))
        
        # Run dijkstras - track (probability, destination)
        """
        Dijkstras can be run with a lazy deletion or an eager deletion
        Lazy === the first time we deque something, we record that in shortest
        Eager === We just do a nice little check and continuously update
        """
        heap = [(-1.0, start_node)]
        cost = {i: float('-inf') for i in range(n)}
        while heap:
            negated_cost, node = heapq.heappop(heap)
            # This path is worse
            if -negated_cost < cost[node]:
                continue
            for to_node, weight in graph[node]:
                new_probability = -negated_cost * weight
                # could be a better path
                if new_probability > cost[to_node]:
                    cost[to_node] = new_probability
                    heapq.heappush(heap, (-new_probability, to_node))
        
            
        val = cost[end_node]
        return val if not math.isinf(val) else 0.0
        