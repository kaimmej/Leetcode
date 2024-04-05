class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        inputLength = len(height)
        l, r = 0, inputLength-1
        
        maxLeftArray    = [0] * inputLength
        maxRightArray   = [0] * inputLength
        waterLineArray  = [0] * inputLength

        # MAX LEFT 
        maxLeft = height[l]
        for i in range(inputLength):
            maxLeftArray[i] = maxLeft
            curr = height[i]
            if(curr > maxLeft):
                maxLeft = curr
            
        # print(maxLeftArray)

        # MAX RIGHT 
        maxRight = height[r]
        for i in reversed(range(inputLength)):
            maxRightArray[i] = maxRight
            curr = height[i]
            if(curr > maxRight):
                maxRight = curr
        # print(maxRightArray)

        # WATER LINE ARRAY
        for i in range(inputLength):
            waterLineArray[i] = min(maxLeftArray[i], maxRightArray[i])

        # print(f"{waterLineArray=}")
        output = 0
        for i in range(inputLength):
            depth = waterLineArray[i] - height[i]
            if depth > 0:
                output += depth
        
        return output