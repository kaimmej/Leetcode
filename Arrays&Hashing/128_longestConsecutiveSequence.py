class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        numberSet = set(nums)
        print(numberSet)
        longestSequence = 0

        for number in nums:
            # does the number-1 exist in the set... if yes, then this is not the beginning of a sequence. We proceed to the next. 
            if number-1 in numberSet:
                continue
            
            # If this is the first number in the sequence, we create a while loop.
            # while the sequence keeps continuing, we want to count the number of items in the sequence, 
            runningSequenceCount = 0 
            currentNumber = number
            while( currentNumber in numberSet):
                currentNumber += 1
                runningSequenceCount += 1
                # print("CONTAINS")
            # print(currentNumber)
            # print(runningSequenceCount)
            longestSequence = max(longestSequence, runningSequenceCount)




            # Finally, we compare it to teh longestSequence, and keep the longer of the two. 
        
        return longestSequence