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


class Solution:
    def findMin(self, nums: List[int]) -> int:
        


        # BINARY SEARCH

        l, r = 0, len(nums)-1
        if r==0:
            return nums[0]

        while l <= r:
            m = (l + r) // 2
            left_num = nums[l]
            right_num = nums[r]
            mid_num = nums[m]
            print(f"{mid_num=}")
            if nums[m+1] < mid_num:
                # we have found the pivot.
                return nums[m+1]
            elif nums[m-1] > mid_num:
                # we have found the pivot
                return mid_num
            elif left_num < right_num:
                # normal array, we return the left most number
                return left_num

            elif left_num < mid_num:
                # [3,4,5,1,2] left half is normal, we must search the right.
                l = m+1
            
            elif right_num > mid_num:
                # [5,1,2,3,4] right have is normal, we must search the left
                r = m-1