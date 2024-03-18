

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        #
        #   create two arrays to store the product of all the elements to the left and right of the current element
        output = [1] * (len(nums))
        left = [1] * (len(nums))
        right = [1] * (len(nums))


        product = 1
        # left array containing products
        for i in range(len(nums)):
            left[i] = product
            product *= nums[i]
        # print("left: ", left)
        
        # right array containing products
        product = 1
        for i in range(len(nums)-1, -1, -1):
            right[i] = product
            product *= nums[i]
        # print("right: ", right)

        for i in range(len(nums)):
            output[i] = left[i]*right[i]
        
        return output