# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        result = [0]
        def maxLength(root):
            if root is None:
                return 0
        
            leftLength = maxLength(root.left)
            rightLength = maxLength(root.right)

            result[0] = max(result[0], leftLength + rightLength)

            return max(leftLength, rightLength) + 1
        
        maxLength(root)
        return result[0]