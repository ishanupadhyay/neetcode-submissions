# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root is None:
            return False
        
        if subRoot is None:
            return True

        def isSameTree (s, t):

            if s is None and t is None:
                return True
            
            if s is None or t is None:
                return False
            
            leftsubtree = isSameTree(s.left, t.left)
            rightsubtree = isSameTree(s.right, t.right)

            if s.val == t.val and leftsubtree and rightsubtree:
                return True
            
            return False
        

        
        return (isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        
        