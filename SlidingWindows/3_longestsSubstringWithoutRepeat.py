class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
            return 0
        print(f"{s=}")
        length = len(s)
        charSet = set()
        left = 0
        right = 1
        best = 1
        charSet.add(s[left])        # we add the left because we need to include the left pointer. 

        while (right < length):
            currentChar = s[right]
            # print(f"{currentChar=}")
            if currentChar in charSet:
                # if we have seen this character before 
                charSet.remove(s[left])
                left += 1
            else:
                # we have not seen this character before. increment right and update best
                currentBest = right-left+1
                if currentBest > best:
                    best = currentBest
                charSet.add(currentChar)
                right += 1
            # print(f"{charSet=}")

        # use a hashSet
        return best



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        letterSet = set()
        maxSequenceLength = 0
        stringLength = len(s)

        if stringLength < 1:
            return maxSequenceLength

        left, right = 0, 0

        while right < stringLength:
            # is right pointing at a new character?
            currChar = s[right]

            if currChar in letterSet:
                # pop ... a number of letters... but dont know how many. 
                # We dont want to pop until we reach right... we wnat to pop until there is no longer a conflict with right. 
                # until we pop currChar... 
                while currChar in letterSet:
                    letterSet.remove(s[left])
                    left += 1
            
            # else:
                # add to the letter set and calculate the new max
                # letterSet.add(currChar)
                # currSequenceLength = right-left
                # maxSequenceLength = max(currSequenceLength, maxSequenceLength)
            letterSet.add(currChar)
            currSequenceLength = right-left + 1
            # print(currSequenceLength)
            # print(f"{left=} : {right=}")
            maxSequenceLength = max(currSequenceLength, maxSequenceLength)
            right += 1
        
        return maxSequenceLength