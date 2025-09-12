# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        prefix_p = self.createPrefixNotation(p)
        prefix_q = self.createPrefixNotation(q)

        return prefix_p == prefix_q
    


    def createPrefixNotation(self, root: Optional[TreeNode]):

        stack = []
        result = []
        if not root:
            return result
        stack.append(root)

        while stack:
            curr = stack.pop()

            result.append(curr.val)

            if curr.left:
                stack.append(curr.left)
            else:
                result.append(None)
            if curr.right:
                stack.append(curr.right)
                result.append(None)



        
        return result
        

        