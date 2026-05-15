# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        1. Define a recursive function that accepts a largest value seen so far param
        2. If a node is good, increment our non_local result counter
        3. Return
        """

        total_good_node_counter: int = 0
        def dfsForGoodNodes(node: Optional[TreeNode], largest_seen_so_far: float) -> None:
            nonlocal total_good_node_counter
            if not node:
                return
            if node.val >= largest_seen_so_far:
                total_good_node_counter += 1

            new_largest = max(largest_seen_so_far, node.val)
            dfsForGoodNodes(node.left, new_largest)
            dfsForGoodNodes(node.right, new_largest)

        dfsForGoodNodes(root, float('-inf'))
        return total_good_node_counter

