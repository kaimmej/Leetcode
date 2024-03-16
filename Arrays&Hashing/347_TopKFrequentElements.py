class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        output = []

        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        # sort the dictionary by the count of its values
        # count = {k: v for k, v in sorted(count.items(), key=lambda item: item[1], reverse=True)}   
        sortedCount = sorted(count.items(), key=lambda x:x[1], reverse=True)  


        for i in range(k):
            output.append(sortedCount[i][0])

        
        return output