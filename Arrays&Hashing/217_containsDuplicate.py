class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
                
        numSet = set()

        for  n in nums :
            if n in numSet:
                return True
            else:
                numSet.add(n)
        
        return False