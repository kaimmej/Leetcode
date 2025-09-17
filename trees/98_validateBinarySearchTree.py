# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root) -> bool:

        # Recursion...
        if not root:
            return True 
        print(root.val)
        # Recursivley call 
        return self.isValidBST_SubTree(root.left, upperBound=root.val, lowerBound=None) and self.isValidBST_SubTree(root.right, lowerBound=root.val, upperBound=None)


    def isValidBST_SubTree(self, root, upperBound, lowerBound):

        if not root:
            return True
        
        # Is the current Node within the upper and lower bound? 
        val = root.val
        # print(val)
        print(f"{lowerBound=} : {val} : {upperBound=}")
        # Short circuit, check if the conditions are false first... and then quickly return False... that way we stop the recursion on one side... 
        # if (upperBound and val >= upperBound) or (lowerBound and val <= lowerBound):
        if (upperBound is not None and val >= upperBound) or (lowerBound is not None and val <= lowerBound):
            # print(f"BOUNDARY")
            return False



        return (
            self.isValidBST_SubTree(root.left, lowerBound=lowerBound, upperBound=val) and 
            self.isValidBST_SubTree(root.right, lowerBound=val, upperBound=upperBound)
        )
            

        