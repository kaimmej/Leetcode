class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        if not word1:
            return word2
        if not word2:
            return word1

        returnString = ""
        word1Length = len(word1)


        for i in range(word1Length):
            returnString += word1[i]
            if i < len(word2):
                returnString += word2[i]
        
        if word1Length < len(word2):
            returnString += word2[word1Length:]
        
        return returnString
        