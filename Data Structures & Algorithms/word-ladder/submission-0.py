class Solution:
    def isOneAway(self, a: str, b: str) -> bool:
        if len(a) != len(b):
            return False
        had_delta = False
        for x, y in zip(a, b):
            if x == y:
                continue
            if had_delta:
                return False
            had_delta = True
        return True



    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Create undirected graph
        graph: Dict[str, Set[str]] = collections.defaultdict(set)
        wordList.append(beginWord)
        for i in range(len(wordList)):
            w1 = wordList[i]
            for j in range(i + 1, len(wordList)):
                w2 = wordList[j]
                if self.isOneAway(w1, w2):
                    graph[w1].add(w2)
                    graph[w2].add(w1)
        
        # Shortest path traversal within undirected graph
        queue = collections.deque([beginWord])
        seen = set([beginWord])
        transformations_performed = 1
        while queue:
            available_transformations = len(queue)
            for _ in range(available_transformations):
                item = queue.popleft()
                if item == endWord:
                    return transformations_performed
                for neighbor in graph[item]:
                    if neighbor not in seen:
                        queue.append(neighbor)
                        seen.add(neighbor)
            # The neighbor set is the available transformations
            transformations_performed += 1
            
        return 0


        