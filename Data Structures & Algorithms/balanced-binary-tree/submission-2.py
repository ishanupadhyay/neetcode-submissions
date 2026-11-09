# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]
        def difference(root):

            if root is None:
                return 0
            
            leftlength = difference(root.left)
            rightlength = difference(root.right)

            if abs(leftlength - rightlength) > 1:
                balanced[0] = False
            
            return max(leftlength, rightlength) + 1

        difference(root)
        return balanced[0]
