class Solution:
    # https://leetcode.com/problems/majority-element/
    # Given an array of size n, find the majority element.
    # The majority element is the element that appears more than n / 2 times.
    # You may assume that the majority element always exists in the array.
    # Example 1:
    # Input: [3,2,3]
    # Output: 3
    # Example 2:
    # Input: [2,2,1,1,1,2,2]
    # Output: 2    
    def majorityElement(self, nums: List[int]) -> int:
        # You can assume the majority element always exists...
        # You can assume the majority element always exists... 

        # dictionary to store the elements we encounter. 
        dict = {}

        # iterate through and add to the dictionary
        for i in range(len(nums)):
            # dictionary get or update? 
            num = nums[i]
            dict[num] = dict.get(num,0) + 1

        # find, and return, the majority element
        # print(dict)
        # calculate the half-way point
        pivot = len(nums)//2
        
        for k, v in enumerate(dict):
            # print(k,v, dict[v])
            if dict[v] > pivot:
                return v

        return 0