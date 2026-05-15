class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Calculate the indegree for everyone
        trust_graph: Dict[int, List[int]] = collections.defaultdict(list)
        in_degree: List[int] = [0] * n
        for a, b in trust:
            # Normalize everything to 0 indexed
            trust_graph[a - 1].append(b - 1)
            in_degree[b - 1] += 1
        
        for i, num_trusted_by in enumerate(in_degree):
            if num_trusted_by == n - 1 and i not in trust_graph:
                return i + 1
        return -1
        
