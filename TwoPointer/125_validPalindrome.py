class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s)-1

        while left < right: 
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
                
        return True


# STACK solution
class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Clean the input data... 
        # Everything needs to be lowercase
        input_lowerCase = s.lower()

        # Remove all non-alpha characters 
        input_alphaLowerCase = re.sub(r'[^A-Za-z0-9]', '', input_lowerCase) # This is saying "anything not a alpha character, replace with empty "" "
        s = []
        # Add everything to a stack... 
        for i in range(len(input_alphaLowerCase)):
            # Add to the stack
            s.append(input_alphaLowerCase[i])
        
        # Iterate and compare characters... forwards and backwards
        for i in range(len(input_alphaLowerCase)):
            end_character = s.pop()
            front_character = input_alphaLowerCase[i]
            if end_character != front_character:
                return False
        return True
        