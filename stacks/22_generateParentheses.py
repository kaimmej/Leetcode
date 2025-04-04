class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        stack = []
        res = []


        def backtrack(openN, closedN):
            if openN == n and closedN == n:
                # print(stack)
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                # print(stack)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                # print(stack)
                stack.pop()
        
        backtrack(0,0)
        return res