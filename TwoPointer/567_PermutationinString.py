class Solution(object):
    
    
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        # early exit
        if not s1:
            return False
        if not s2:
            return False

        # create variables
        l, r = 0,0 

        # create a dictionary of the first string
        s1Dict = {}
        for c in s1:
            if c in s1Dict:
                s1Dict[c] += 1
            else:
                s1Dict[c] = 1

        #
        #
        #
        windowLength = len(s1)
        lastWindowPosition = len(s2) - len(s1)
        # there might be an off-by-one issue here.. will come back. 

        # loop through the second string
        while l <= lastWindowPosition:
            currentChar = s2[l]
            r = l + windowLength - 1
            currentWindow = s2[l:r+1]

            
            # print(f"{l=}:{r=} :: {currentChar=} :: {currentWindow=}")
            # print(f"{windowLength=}")

            # is currentChar in the s1 dictionary? 
            if currentChar in s1Dict:

                # if it is, then we need to compare the window the permutation we are looking for? 
                if self.compareMapToString(s1Dict.copy(), currentWindow):
                    return True

            l += 1
        return False


    def compareMapToString(self, map, string):
        for c in string:
            if c in map:
                map[c] -= 1
                if map[c] == 0:
                    del map[c]
            else:
                return False
        return len(map) == 0