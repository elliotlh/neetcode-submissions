from dataclasses import dataclass
from typing import Tuple

@dataclass(order=True)
class FlightEdge:
    cost: int
    to_airport: int

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        1. We need to turn flights into a directed, weighted graph. We will use an adjacency list
        2. We need to run dijkstras sorted path algorithm with src and dst
                special problem constraint: if adding a neighbor puts us over k, we simply cannot add that neighbor
        3. We will store the shortest path in a shortest dict, and if the key is set, we can return that, otherwise
                it must be impossible and we return -1


        Step 2 breakdown: Dijkstras
        1. We need a min heap to keep track of (cost_to_get_here, edges_to_get_here, node_id)
        2. We start at src, add all neighbors that qualify (e.g. don't go over K boundary) to min heap
        3. We pop our best option from the minheap. If there is no shortest for this node, we can add it,
                Otherwise, someone else got here first and we already know we have a cheaper path here because
                the min heap property guarantees correct traversal ordering
        """

        flight_graph: Dict[int, List[FlightEdge]] = collections.defaultdict(list)
        for src_airport, dst_airport, cost in flights:
            flight_graph[src_airport].append(FlightEdge(cost, dst_airport))

        # min heap keeps track of
        # flight_edge, cumulative cost, total layovers to reach
        min_heap: List[Tuple[int, FlightEdge, int]] = []
        for neighbor in flight_graph[src]:
            heapq.heappush(min_heap, (neighbor.cost, neighbor, 0))
        while min_heap:
            total_cost, node, layovers_to_reach = heapq.heappop(min_heap)
            if node.to_airport == dst:
                return total_cost
                
            for neighbor in flight_graph[node.to_airport]:
                if layovers_to_reach < k:
                    heapq.heappush(min_heap, (total_cost + neighbor.cost, neighbor, layovers_to_reach + 1))
        return -1





        