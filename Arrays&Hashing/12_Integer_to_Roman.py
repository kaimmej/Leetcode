class Solution:
    def intToRoman(self, num: int) -> str:

        return_String = ""
        values = {
            1000 : "M",
            900 : "CM",
            500 : "D",
            400 : "CD",
            100 : "C",
            90 : "XC",
            50 : "L",
            40 : "XL",
            10 : "X",
            9 : "IX",
            5 : "V",
            4 : "IV",
            1 : "I"
        }


        while num > 0:

            
            # Find the largest number that could be subtracted from num, subtract the number and add the cooresponding Symbol to the return string.
            notFound = True
            largestNumber = 0
            symbol = ""
            # print(num)
            for key in values:
                # Iterate through the values dictionary
                currNumber = key
                currSymbol = values[currNumber]
                # print(f"   {currNumber}")

                # Can it be subtracted from Num? And is it larger than the current largestNumber? 
                # If yes, then it is our newest. 
                if num >= currNumber and currNumber > largestNumber:
                    symbol = currSymbol
                    largestNumber = currNumber

            num = num - largestNumber
            return_String += symbol
            # print(f"   {symbol} : {largestNumber}")
        

        # What is the largest number that we could subtract from this? 

        
        return return_String