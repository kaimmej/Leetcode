class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        """

        res = ""

        # We need to tell it, how many letters are in this word... and encode a character after that number. 
        # Enocded character will be "_". So it will look like "5_Hello"
        
        for word in strs:
            print(word)
            wordLength = len(word)
            res = res + str(wordLength) + "_" + word
        
        print(res)
        # return res[1:]
        return res

    def decode(self, s):
        """Decodes a single string to a list of strings.
        """
        if len(s) == 0:
            return [""]

        listStrings = []

        
        curr = 0
        while curr < len(s):
            # Break condition. No more letters to ingest
            if curr >= len(s):
                break


            # Parse the first characters of each word. 
            # They tell us how long the word will be, and how many characters we need to ingest. 
            tempWord = ""
            tempChar = s[curr]
            letterCount = ""

            # read until we reach a "_"
            while tempChar != "_":
                letterCount += tempChar
                curr += 1
                tempChar = s[curr]


            curr += 1 # we want to now discard the "_"
            wordLength = int(letterCount)
