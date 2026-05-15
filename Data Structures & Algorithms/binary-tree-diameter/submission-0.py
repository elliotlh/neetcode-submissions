# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.result = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.result

    def traverse(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = self.traverse(root.left)
        right_depth = self.traverse(root.right)
        self.result = max(left_depth + right_depth, self.result)
        return max(1 + left_depth, 1 + right_depth)
        
        