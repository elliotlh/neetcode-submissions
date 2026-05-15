# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        from a given root, are p and q in different subtrees?
            if yes: i must be the LCA because I am the branch point
        if there is only 1 possible branch:
            am I p or q?
                if yes, then return p or q
            otherwise, go down the branch and try again
        """
        needs_traverse_left, needs_traverse_right = False, False
        # Is the current root the branching point between p and q? It must necessarily be the answer
        if root.val != p.val and root.val != q.val:
            print('getting here')
            if p.val < root.val or q.val < root.val:
                needs_traverse_left = True
            if p.val > root.val or q.val > root.val:
                needs_traverse_right = True
            print(root.val, p.val, q.val, needs_traverse_left, needs_traverse_right)
            if needs_traverse_left and needs_traverse_right:
                return root
        
        # is the current root one of the targets? If so, thats always the LCA
        if root.val == p.val or root.val == q.val:
            print('returning root here')
            return root
        # Otherwise the answer must be in one of the calculated branches
        if needs_traverse_left:
            print('traversed left')
            assert root.left
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            print('traversed right')
            assert root.right
            return self.lowestCommonAncestor(root.right, p, q)
        
            
        