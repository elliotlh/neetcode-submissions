class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    def find(self, n: int) -> int:
        # path compression. If we are not our own parent, we must be at the bottom or middle of the tree
        if self.parent[n] != n:
            # this is important, this means as we walk up the tree, we set each node's parent to the top
            # this keeps the tree flat
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, x: int, y: int) -> bool:
        x_parent, y_parent = self.find(x), self.find(y)
        if x_parent == y_parent:
            # they are already unioned
            return False
        
        # if x is shorter than y, lets attach x to y so there is no net height change
        if self.rank[x_parent] < self.rank[y_parent]:
            self.parent[x_parent] = y_parent
        # if y < x, lets attach y to x so net height doesn't change
        elif self.rank[y_parent] < self.rank[x_parent]:
            self.parent[y_parent] = x_parent
        else:
            # otherwise we just gotta pick one
            # we attach y to x, then x has a bigger rank 
            self.parent[y_parent] = x_parent
            self.rank[x_parent] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        candidate: List[int] = []
        for edge in edges:
            # if we couldn't union them, its already duplicated
            if not uf.union(edge[0], edge[1]):
                candidate = edge
        return candidate
        