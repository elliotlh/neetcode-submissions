# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        biggest_path = float('-inf')
        def maxPathSumFromNode(node: Optional[TreeNode]) -> int:
            nonlocal biggest_path
            if not node:
                return 0
            max_left = maxPathSumFromNode(node.left)
            max_right = maxPathSumFromNode(node.right)
            # these our the biggest paths that can lead to a bigger path
            biggest_path_through_root = max(
                node.val, 
                max_left + node.val, 
                max_right + node.val,
            )
            # these are the biggest paths, including a non-returnable path where the root is summed with max left and right
            # this is not returnable because path sum cannot be branching
            biggest_path = max(biggest_path, biggest_path_through_root, node.val + max_left + max_right)
            return biggest_path_through_root
        maxPathSumFromNode(root)
        return biggest_path