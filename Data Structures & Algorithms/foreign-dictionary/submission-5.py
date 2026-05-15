from typing import Tuple
class Solution:
    def __init__(self):
        self.debug = True

    def log(self, *args):
        if self.debug:
            pass

    def getEdge(self, a: str, b: str) -> Tuple[List[str], bool]:
        small = min(len(a), len(b))
        for i in range(small):
            if a[i] != b[i]:
                return [a[i], b[i]], True
        if len(a) <= len(b):
            return [], True
        return [], False

    def foreignDictionary(self, words: List[str]) -> str:
        """
        Idea:
        1. We can build a graph from each word, and then from the relative position of each word
        2. This should give us a DAG, upon which we can use topsort
        """
        graph: Dict[str, Set[str]] = collections.defaultdict(set)
        char_set: Set[str] = set()
        in_degree: Dict[str, int] = collections.defaultdict(int)

        for word in words:
            for char in word:
                char_set.add(char)

        for i in range(len(words) - 1):
            edge, valid = self.getEdge(words[i], words[i+1])
            if not valid:
                return ''
            if edge and edge[1] not in graph[edge[0]]:
                graph[edge[0]].add(edge[1])
                in_degree[edge[1]] += 1

        # Now lets run kahns algorithm to generate a topological sort
        queue = collections.deque()
        for key in char_set:
            if in_degree[key] == 0:
                queue.append(key)

        top_sort: List[str] = []
        while queue:
            popped = queue.popleft()
            top_sort.append(popped)
            for neighbor in graph[popped]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return ''.join(top_sort) if len(top_sort) == len(char_set) else ''