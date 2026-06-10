from functools import cache
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = collections.defaultdict(list)
        for prerequisite, course in prerequisites:
            graph[prerequisite].append(course)

        @cache
        def dfs(from_node, to_node) -> bool:
            if from_node == to_node:
                return True
            for neighbor in graph[from_node]:
                if dfs(neighbor, to_node):
                    return True
            return False
        
        out = []
        for a, b in queries:
            out.append(dfs(a, b))
        return out


        

        