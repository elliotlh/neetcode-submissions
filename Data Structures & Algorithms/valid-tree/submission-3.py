class UnionFind:
    def __init__(self, n) -> None:
        self.parent: Dict[int, int] = {}
        self.rank: Dict[int, int] = {}
        self.independent_components = n
        # Everyone is their own disjoint set
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 1
    
    def find(self, x: int) -> int:
        if self.parent[x] == -1:
            raise ValueError('not in data structure')
        # If I'm not the root, perform path compression
        # by walking up the tree and pointing every node
        # on the way up to the top level parent
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x == parent_y:
            return False
        # If we union, we are joining 2 independent components together
        self.independent_components -= 1
        # If x < y, then attach x to y
        if self.rank[parent_x] < self.rank[parent_y]:
            self.parent[parent_x] = parent_y
        # otherwise if x > y, attach y to x as the root
        elif self.rank[parent_x] > self.rank[parent_y]:
            self.parent[parent_y] = parent_x
        # otherwise pick one, and then make sure the rank is adjusted
        else:
            self.parent[parent_x] = parent_y
            self.rank[parent_y] = self.rank[parent_y] + 1
        return True

    def all_joined(self) -> bool:
        return self.independent_components == 1


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)
        for a, b in edges:
            if not uf.union(a, b):
                return False
        return uf.all_joined()
        