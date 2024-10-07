class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        inputLength = len(nums)
        answerLength = 2 * inputLength 
        ans = [1] * answerLength

        for i in range(inputLength ):
            val = nums[i]
            ans[i] = val 
            ans[i + inputLength] = val 
        print(ans)

        return ans