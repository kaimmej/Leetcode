# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root) -> bool:
        self.balancedTree = True

        if not root:
            return True
        self.dfs(root)

        return self.balancedTree
    
    def dfs(self, curr):
        flag_balanced = True
        if not curr: 
            return flag_balanced, 0
        
        left_balance, left = self.dfs(curr.left)
        right_balance, right = self.dfs(curr.right)
        maxHeight = max(left, right)

        # we compare the heights
        diff = abs(left-right)
        print(f" {curr.val} : {flag_balanced} : {left} : {right} ")
        if abs(left-right) > 1:
            self.balancedTree = False

        # if diff is greater than 1 ... it is not balanced
        return flag_balanced, 1 + maxHeight
        