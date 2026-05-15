"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        original_to_clone = {}
        self.createClones(node, original_to_clone)
        for k,v in original_to_clone.items():
            print(k.val, v.val)
        self.createNeighbors(node, original_to_clone)
        return original_to_clone[node]

    def createNeighbors(self, node: Optional[Node], original_to_clone: Dict[Node, Node]) -> None:
        if not node:
            return None
        queue: deque[Node] = collections.deque([node])
        visited = set([node])
        while queue:
            current_node = queue.popleft()
            cloned_node = original_to_clone[current_node]
            for neighbor in current_node.neighbors:
                cloned_node.neighbors.append(original_to_clone[neighbor])
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        return

                
                


    def createClones(self, node: Optional[Node], original_to_clone: Dict[Node, Node]) -> None:
        if not node:
            return
        if node in original_to_clone:
            return
        cloned = Node(node.val)
        original_to_clone[node] = cloned
        for neighbor in node.neighbors:
            self.createClones(neighbor, original_to_clone)
            
        