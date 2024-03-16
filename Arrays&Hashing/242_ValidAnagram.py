class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        
        # create a dictionary to count the letters of each string. 
        countS, countT = {}, {}

        for c in range(len(s)):
            countS[s[c]] = 1+ countS.get(s[c], 0)
        for c in range(len(t)):
            countT[t[c]] = 1+ countT.get(t[c], 0)

        # if the length of the strings are different, they can't be anagrams
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True
    
    #
    # Second approach uses a single dictionary to count the letters of each string. So less memory.
    def isAnagram2(self, s, t):
        if len(s) != len(t):
            return False

        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1

        for c in t:
            if c not in count:
                return False
            count[c] -= 1
            if count[c] == 0:
                del count[c]

        return len(count) == 0  