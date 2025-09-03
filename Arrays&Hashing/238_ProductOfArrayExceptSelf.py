

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


    def productExceptSelf(self, nums):
        
        arrayLength = len(nums)
        if arrayLength <= 1:
            return nums

        preArray = [1] * arrayLength
        postArray = [1] * arrayLength
        returnArray =  [1] * arrayLength

        # Two passes through
        # First pass... backwards from the end
        #   - multiply, and keep track of everything we have seen so far.
        #   preArray
        
        # Second array... multiply elements seen so far together
        #   postArray

        # print(preArray)
        # print(postArray)

        for i in range(arrayLength-2, -1, -1):
            # print(f" {i} : {nums[i]} : {preArray[i]}")
            preArray[i] = preArray[i+1] * nums[i+1]


        for i in range(1, arrayLength):
            postArray[i] = postArray[i-1] * nums[i-1]

        # print(postArray)

        for i in range(arrayLength):
            # print(f" {i} : {postArray[i]} : {preArray[i]}")
            returnArray[i] = postArray[i] * preArray[i]
        
        return returnArray