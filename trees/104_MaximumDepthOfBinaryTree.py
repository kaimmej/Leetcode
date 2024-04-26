# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        
        if root is None:
            return 0

        depth = 0

        leftTreeDepth = 1 + self.maxDepth(root.left)
        rightTreeDepth = 1 + self.maxDepth(root.right)

        # max of the two
        depth = max(leftTreeDepth, rightTreeDepth)
        return depth