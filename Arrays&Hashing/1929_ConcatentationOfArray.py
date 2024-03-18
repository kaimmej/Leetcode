class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        output = [0] * (length*2)

        for i in range(length):
            output[i] = nums[i]
            output[i+length] = nums[i]
        
        return output