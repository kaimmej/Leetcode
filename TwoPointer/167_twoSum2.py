class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
                
        arrayLength = len(numbers)

        left, right = 0, arrayLength-1
        while left < right: 
            # for this number, I want to iterate down the rest of the array, and see if this is equal to the target. 
            leftNum = numbers[left]
            rightNum = numbers[right]

            sumNumber = leftNum + rightNum
            if sumNumber == target:
                return [left+1, right+1]
            elif sumNumber > target:
                right -= 1

            else:
                left += 1
        return [0]
