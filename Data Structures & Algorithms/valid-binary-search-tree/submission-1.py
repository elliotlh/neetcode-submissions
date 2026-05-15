# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isNodeWithinBounds(node: Optional[TreeNode], lower_bound: int, upper_bound: int) -> bool:
            if not node:
                return True
            if node.val <= lower_bound or node.val >= upper_bound:
                return False
            return (
                isNodeWithinBounds(node.left, lower_bound, min(upper_bound, node.val))
                and
                isNodeWithinBounds(node.right, max(lower_bound, node.val), upper_bound)
            )
        return isNodeWithinBounds(root, -10000, 10000)
        