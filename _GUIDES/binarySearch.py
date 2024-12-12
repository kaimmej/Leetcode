


# REQUIREMENTS 
#   - Must be sorted. 


# BINARY SEARCH SPLITS AT THE MIDDLE... and asks "is what I am seeking in the first half? or the second?". It keeps doing that until it finds it. 
    def search(self, nums, target):

        if not nums:
            return -1

        numsLength = len(nums)
        l, r = 0, numsLength-1


        while l <= r:
            mid = (l+r)//2
            # print(f"{mid=}")
            # print(f"{l=}")
            # print()
            n = nums[mid]
            if n > target:
                r = mid - 1
            # the target is to the right of middle
            elif n < target:
                l = mid + 1
            else:
                return mid
        
        return -1