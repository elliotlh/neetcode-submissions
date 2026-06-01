class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        graph = collections.defaultdict(list)
        for requisite, requires in prerequisites:
            in_degree[requisite] += 1
            graph[requires].append(requisite)
        queue = collections.deque([c for c in range(numCourses) if in_degree[c] == 0])
        top_sort = []
        while queue:
            course = queue.popleft()
            top_sort.append(course)
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return len(top_sort) == numCourses
            
        