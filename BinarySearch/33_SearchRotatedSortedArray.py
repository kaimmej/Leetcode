class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        
        # BINARY SEARCH

        l, r = 0, len(nums)-1

        if r == 0:
            if nums[0] == target:
                return 0
            else:
                return -1

        while l <= r:
            m = (l + r) // 2
            left_num = nums[l]
            right_num = nums[r]
            mid_num = nums[m]

            if target == mid_num:
                return m

            # print("")
            # print(f"{left_num=}")
            print(f"{mid_num=}")
            # print(f"{right_num=}")


            # LEFT SORTED PORTION
            if left_num <= mid_num:
                
                if target > mid_num or target < left_num:
                    l = m+1

                
                #why would this not be true? 
                # - the target is less then middle (move left)
                # - or the target is greater than the left_num... which means the array is sorted and the unsorted portion is to the right (as is the answer)
                else:
                    r = m - 1
            # RIGHT SORTED PORTION 
            else: 
                if target < mid_num or target > right_num:
                    r = m-1
                else:
                    l = m+1
        
        return -1
