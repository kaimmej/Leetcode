import unittest

class TestProductOfArrayExceptSelf(unittest.TestCase):
    def test_example1(self):
        nums = [1, 2, 3, 4]
        expected_output = [24, 12, 8, 6]
        # BEGIN: /Users/jonkaimmer/Documents/GitHub/Leetcode/Arrays&Hashing/238_ProductOfArrayExceptSelf.py
        # Place your code here
        # END: /Users/jonkaimmer/Documents/GitHub/Leetcode/Arrays&Hashing/238_ProductOfArrayExceptSelf.py
        self.assertEqual(actual_output, expected_output)

    def test_example2(self):
        nums = [-1, 1, 0, -3, 3]
        expected_output = [0, 0, 9, 0, 0]
        # BEGIN: /Users/jonkaimmer/Documents/GitHub/Leetcode/Arrays&Hashing/238_ProductOfArrayExceptSelf.py
        # Place your code here
        # END: /Users/jonkaimmer/Documents/GitHub/Leetcode/Arrays&Hashing/238_ProductOfArrayExceptSelf.py
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()