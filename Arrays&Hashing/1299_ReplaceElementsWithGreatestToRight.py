class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if not arr or len(arr) == 0:
            return []
        


        # Iterate backwards ... and keep track of the greatest element.
        lengthArray = len(arr)
        res = [-1] * lengthArray
        maxSeen = -1

        for i in range(lengthArray-1, -1, -1):

            res[i] = maxSeen

            maxSeen = max(maxSeen, arr[i])
            # print(f" {arr[i]} : {maxSeen}" )
        
        return res
        