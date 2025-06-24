class Solution:
    def romanToInt(self, s: str) -> int:
        
        conversion_dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L"  : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000   
        }

        result = 0
        i = 0
        string_length = len(s)

        # Iterate left to right
        while i < len(s):

            # If there are two letters left AND the value of the second is greater than the value of current
            if len(s)-i > 1 and conversion_dict[s[i]] < conversion_dict[s[i+1]]:
                # combine current and next... and add the subtracted number to the result. 
                result += (conversion_dict[s[i+1]] - conversion_dict[s[i]])

                # Increment by two
                i += 2

            # Otherwise
            else:
                result += conversion_dict[s[i]]
                i += 1

        return result