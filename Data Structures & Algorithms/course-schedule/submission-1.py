class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            graph[a].append(b)
            in_degree[b] += 1
        
        queue = collections.deque([i for i in range(numCourses) if in_degree[i] == 0])
        topological_count = 0
        while queue:
            course = queue.popleft()
            topological_count += 1
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return True if topological_count == numCourses else False
        