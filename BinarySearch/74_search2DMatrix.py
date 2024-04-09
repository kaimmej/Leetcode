class Solution:
    def searchMatrix(self, matrix, target):
        
        # this is a double binary search problem... 
        # first we find the row, and then we must search that row. 


        l, r = 0, len(matrix)-1
        width = len(matrix[0])
        targetRow = 0
        while l <= r:
            mid = (l+r)//2
            lowNum = matrix[mid][0] 
            highNum = matrix[mid][width-1] 
            # print(f"{mid=}")
            if lowNum > target:
                r = mid-1
            elif highNum < target:
                l = mid+1
            else:
                # this is the correct row
                targetRow = mid
                break
        # print(f"{targetRow=}")
        # now we need to search the row
        l,r = 0, width-1
        while l <= r: 
            mid = (l+r)//2  
            n = matrix[targetRow][mid]

            if n > target:
                r = mid-1
            elif n < target:
                l = mid+1
            else:
                return True
        
        return False