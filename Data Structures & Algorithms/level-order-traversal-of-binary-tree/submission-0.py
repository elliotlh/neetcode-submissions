from typing import Deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(Deque, self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue: Deque[TreeNode] = collections.deque([root])
        result: List[List[int]] = []
        while queue:
            num_in_level = len(queue)
            level_nodes: List[int] = []
            for nodes in range(num_in_level):
                node = queue.popleft()
                level_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_nodes)
        return result
        