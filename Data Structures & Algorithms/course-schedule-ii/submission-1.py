class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        1. Turn prerequisites into an adj list
        2. Set all the in-degrees of each course
        3. Create a BFS starting from all nodes with 0 in-degree
        4. Visit all nodes, when adding a node to the visited set,
                ensure that we correctly decrement in the in-degree
        5. If len(sorted_list) != numCourses:
                return []
        6. Return sorted_list
        """

        course_graph = collections.defaultdict(list)
        in_degree = collections.defaultdict(int)
        for blocked_by, course in prerequisites:
            course_graph[course].append(blocked_by)
            in_degree[blocked_by] += 1
        queue = collections.deque([course for course in range(numCourses) if in_degree[course] == 0])
        valid_course_ordering: List[int] = []
        while queue:
            popped = queue.popleft()
            valid_course_ordering.append(popped)
            for neighbor in course_graph[popped]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return valid_course_ordering if len(valid_course_ordering) == numCourses else []