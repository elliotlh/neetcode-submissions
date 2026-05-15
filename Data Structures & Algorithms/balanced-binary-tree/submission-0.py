# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced: bool = True
        def getHeightFromNode(node: Optional[TreeNode]) -> int:
            nonlocal balanced
            if not node:
                return 0
            # early execution
            if not balanced:
                return 0
            left = getHeightFromNode(node.left)
            right = getHeightFromNode(node.right)
            if abs(left - right) > 1:
                balanced = False
            # my heigh is the bigger of my two subtrees
            return 1 + max(left, right)
        getHeightFromNode(root)
        return balanced

        
        