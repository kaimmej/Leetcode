class Solution:
    
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums)-1
        mid = 0

        while left<=right:

            mid = (left+right)//2

            if (nums[left] <= nums[mid]):
                # if the first number is less than the middle number, we know that the left part of hte array is normally ordered relative to the middle. 
                # we need to check if the entire array is normal, or whether the rotated, pivot point (and minimum) are in the right section of the array. 
                if nums[mid]<=nums[right]:
                    return nums[left]
                else:
                    left = mid+1

            else:
                # The pivot is in the left portion of the array
                right = mid

        return mid
        