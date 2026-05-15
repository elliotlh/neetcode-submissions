# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
            6
        4       9
      2   5   7   12
    """
    def __init__(self):
        self.processed = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        val = self.kthSmallest(root.left, k)
        if val != -1:
            return val
        self.processed += 1
        if self.processed == k:
            return root.val
        val = self.kthSmallest(root.right, k)
        if val != -1:
            return val
        return -1