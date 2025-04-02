    def removeElement(self, nums: List[int], val: int) -> int:
        # val (int) -- we want to remove all occurances
        # nums (int array) -- remove val from here.
        #    - order can change
        quantity = 0
        i = 0
        while i < len(nums):
            num = nums[i]
            print(num)
            if num == val:
                # if this index equates to the value of val, delete it. 
                del nums[i]
                i = i-1
            else:
                quantity += 1
            i += 1



        # return number of elements in nums that are not equal to val
        return quantity