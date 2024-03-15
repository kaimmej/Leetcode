class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answerDictionary = {}

        for i, num in enumerate(nums):

            #
            #   iterate over the numbers within the number array. For each, store the the requiredNextValue:index of first
            required = target - num

            # print("required: ", required)
            # print(answerDictionary)
            # print(required in answerDictionary)


            # is requried already within the dictionary? if yes return its index+current index.
            if required in answerDictionary:
                return [answerDictionary.get(required),i] 
                
            else:
                answerDictionary[num] = i