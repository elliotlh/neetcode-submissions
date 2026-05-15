class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for ui, vi, ti in times:
            graph[ui].append((vi, ti))
        min_cost_to_reach = {}

        def dfs(node: int, current_time: int) -> None:
            if current_time >= min_cost_to_reach.get(node, float('inf')):
                return
            min_cost_to_reach[node] = current_time
            for neighbor, time in graph[node]:
                dfs(neighbor, current_time + time)

        dfs(k, 0)
        return -1 if len(min_cost_to_reach) < n else max(min_cost_to_reach.values())
        