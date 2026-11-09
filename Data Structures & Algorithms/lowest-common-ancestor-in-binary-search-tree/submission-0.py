# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        if root is None:
            return None
        
        if root is p or root is q:
            return root
        
        leftnodesearch = self.lowestCommonAncestor(root.left, p, q)
        rightnodesearch = self.lowestCommonAncestor(root.right, p, q)

        if leftnodesearch and rightnodesearch is None:
            return leftnodesearch
        if leftnodesearch is None and rightnodesearch:
            return rightnodesearch
        
        if leftnodesearch is None and rightnodesearch is None:
            return None
        
        return root
