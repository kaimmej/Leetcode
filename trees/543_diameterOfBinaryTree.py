# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        if not root:
            return 0

        self.dfs(root)

        return self.result
        

    # Returns the height
    def dfs(self, curr):

        if not curr:
            return 0
        left = self.dfs(curr.left)
        right = self.dfs(curr.right)
        
        self.result = max(self.result, left + right)

        # returns whichever branch is longer... + 1
        return  1 + max(left, right)
        