class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        # we need a dictionary to store the characters of t
        tCharacters = {}
        l = 0
        r = 0
        inputLength = len(s)
        windowLength = len(t)
        lastWindowPosition = inputLength - windowLength

        for c in t:
            if c in tCharacters:
                tCharacters[c] += 1
            else:
                tCharacters[c] = 1


        while l<lastWindowPosition: # WE DONT WANT -1 HERE
            currentChar = s[l]
            # l += 1
            # if currentChar not in tCharacters:
            #     continue

            currentWindow = s[l:l+windowLength]
            print(f"{l=} :: {currentChar=} :: {currentWindow=}")
            print(f"{tCharacters=}")
            print()
            if currentChar in tCharacters:
                if self.compareMapToString(tCharacters.copy(), currentWindow):
                    return currentWindow
            l += 1


    def compareMapToString(self, map, string):
        for c in string:
            if c in map:
                map[c] -= 1
                if map[c] == 0:
                    del map[c]
        return not map