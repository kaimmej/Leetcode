class Solution:
    def isValid(self, s: str) -> bool:
        
        begginingParentheses = [ "{", "(", "["]
        
        closeToOpen = {
            "}":"{",
            ")":"(",
            "]":"["
        }

        stack = []

        for str in s:
            if str in closeToOpen:
                # end character
                if stack and stack[-1] == closeToOpen[str]:
                    # valid, pop the top of hte stack
                    stack.pop()
                else:
                    return False
            else:
                # beggining parentheses... add to stack
                stack.append(str)
                print(str)

        
        print(stack)
        return True if not stack else False