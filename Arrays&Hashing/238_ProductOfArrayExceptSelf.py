import unittest
from solution import productExceptSelf

class TestProductOfArrayExceptSelf(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()  # Create an instance of Solution
    
    def test_example1(self):
        nums = [1, 2, 3, 4]
        expected_output = [24, 12, 8, 6]
        actual_output = solution.productExceptSelf(nums)
        self.assertEqual(actual_output, expected_output)

    def test_example2(self):
        nums = [-1, 1, 0, -3, 3]
        expected_output = [0, 0, 9, 0, 0]
        actual_output = solution.productExceptSelf(nums)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()



class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        #
        #   create two arrays to store the product of all the elements to the left and right of the current element
        left = []
        right = []

        # iterate through the input array and store the product of all elements to the left of the current element
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            left[i] = product

        print(left)


        return 0