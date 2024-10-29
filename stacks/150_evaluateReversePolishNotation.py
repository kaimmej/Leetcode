class Solution:
    def evalRPN(self, tokens: List[str]) -> int:




        stack = []
        for str in tokens:
            if str == '+':
                int1 = stack.pop()
                int2 = stack.pop()
                stack.append(int1 + int2)
            elif str == '-':
                int1 = stack.pop()
                int2 = stack.pop()
                stack.append(int2 - int1)
            elif str == '/':
                int1 = stack.pop()
                int2 = stack.pop()
                stack.append(int(int2 / int1))
            elif str == '*':
                int1 = stack.pop()
                int2 = stack.pop()
                stack.append(int1 * int2)
            else: 
                stack.append(int(str))
            

        print(f"{stack=}")
        return stack.pop()
