class Solution(object):


    # You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
    # Return the length of the longest substring containing the same letter you can get after performing the above operations.
    currentMaxCharacter = ""
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        print(f"{s=}, {k=}")
        # Early exit
        if not s:
            return 0

        charDict = {}
        lengthString = len(s)

        l, r = 0, 0
        best = 1
            # this is not being used. 

        # we move across 
        while r < lengthString:
            # print("")
            # update the window's dictionary
            #   Note: we do this here, so that we do not indexOutOfBounds the right most pointer, we want to check this with the while condition first.
            currentCharacter = s[r]
            # print(f"{currentCharacter=}")
            currentWindow = s[l:r+1]

            windowLength = len(currentWindow)


            # print(f"{l=}:{r=} :: {currentCharacter=} :: {currentWindow=}")
            # print(f"{windowLength=}")
            if currentCharacter in charDict:
                # print("adding:", currentCharacter)
                charDict[currentCharacter] += 1
            else:
                charDict[currentCharacter] = 1

            # print(charDict)
            longest = self.findMaxCharacter(charDict, currentCharacter)
            # print(f"{longest=}")


            # Valid
            if(windowLength - longest <= k):
                r += 1
                if windowLength > best:
                    best = windowLength
            # Invalid
            else:
                # print("Invalid")
                charDict[s[l]] -= 1
                charDict[s[r]] -= 1
                l += 1
        return best
    
    # returns the length of the largest character found in the current window
    # sets current max character to the character that was found
    def findMaxCharacter(self, charDict, currentCharacter):
        # currentMax
        # print(f"{currentCharacter=} :: {self.currentMaxCharacter=}")
        if currentCharacter == self.currentMaxCharacter:
            return charDict[currentCharacter]

        tempLongestChar = ""
        lengthLongest = 0
        for key in charDict:
            current = charDict[key]
            if current > lengthLongest:
                lengthLongest = current
                tempLongestChar = key
        
        # print(f"{tempLongestChar=} :: {lengthLongest=}")
        self.currentMaxCharacter = tempLongestChar
        return lengthLongest
