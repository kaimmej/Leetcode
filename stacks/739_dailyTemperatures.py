class Solution:
    # 
    # BRUTE FORCE, GO FIND THE NEXT HIGHER TEMP
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

    #     tempArrayLength = len(temperatures)
    #     res = [1] * tempArrayLength
    #     for i in range(tempArrayLength):
    #         # print(temperatures[i])
    #         Found = False
    #         cursor = i+1
    #         currentTemp = temperatures[i]
    #         while( not Found):
    #             # print(f"  {cursor=}")
    #             if cursor >= tempArrayLength:
    #                 res[i] = 0
    #                 break
                
    #             if temperatures[cursor] > currentTemp:
    #                 # print(f"  {i=}")
    #                 res[i] = cursor-i
    #                 break
                
    #             cursor += 1

    #     return res
    


        def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # 
        # MONOTONIC DECREASING STACK
        tempArrayLength = len(temperatures)
        res = [0] * tempArrayLength
        stack = [] # pair: [temp, index]

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                # print(f"{stack=}")

                stackTemp, stackIndex = stack.pop()
                # print(f"  {stackTemp=}")
                # print(f"  {stackIndex=}")
                res[stackIndex] = (i - stackIndex)
            stack.append([temp, i])


        return res