class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        # Kahns algo
        graph = collections.defaultdict(list)
        in_degree = [0] * n
        for prev, fut in relations:
            graph[prev - 1].append(fut - 1)
            in_degree[fut - 1] += 1
        
        queue = collections.deque([
            course_id for course_id, degree in enumerate(in_degree) if degree == 0
        ])
        required_semesters = 0
        taken_courses = 0
        while queue:
            required_semesters += 1
            queue_len = len(queue)
            for _ in range(queue_len):
                c = queue.popleft()
                taken_courses += 1
                for neighbor in graph[c]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

        return required_semesters if taken_courses == n else -1
        
        