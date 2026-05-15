class UnionFind:
    def __init__(self, n: int):
        self.parents: Dict[int, int] = {}
        self.rank: Dict[int, int] = {}
        # The UF data structure starts where every node is its own parent
        # and all trees have a rank (depth) of 1
        for i in range(n):
            self.parents[i] = i
            self.rank[i] = 1

    def find(self, node: int) -> int:
        if node not in self.parents:
            return -1
        # Special case: if the node does not equal the parent, then we'll do path compression
        # on the way back up to keep the tree as flat as possible
        if node != self.parents[node]:
            # Logic: We want to point this node to the highest level parent
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, a: int, b: int) -> bool:
        parent_a, parent_b = self.find(a), self.find(b)
        # These are already unioned
        if parent_a == parent_b:
            return False
        # We need to attach the smaller tree to the bigger tree to ensure total tree depth is unchanged
        if self.rank[parent_a] < self.rank[parent_b]:
            self.parents[parent_a] = parent_b
        elif self.rank[parent_b] < self.rank[parent_a]:
            self.parents[parent_b] = parent_a
        else:
            # In this case, we pick an arbitrary join and we increase the rank acordingly
            self.parents[parent_a] = parent_b
            self.rank[parent_b] += 1
        return True

    def get_distinct_parents(self, n: int) -> int:
        distinct_parents: Set[int] = set()
        for i in range(n):
            distinct_parents.add(self.find(i))
        return len(distinct_parents)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Thoughts:
        1. 1 strategy to efficiently find connected components is union find
        2. We can create a UF class and initialize it with N
        3. We can iterate through all our edges and union the edge nodes together
        4. The distinct number of "parents" in the UF data structure will be our output
                since those will be disconnected components
        """
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)
        return uf.get_distinct_parents(n)        