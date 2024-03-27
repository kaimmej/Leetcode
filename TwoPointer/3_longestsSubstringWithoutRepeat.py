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