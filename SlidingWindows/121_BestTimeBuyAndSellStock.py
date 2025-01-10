class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
                
        l=0
        r=0
        bestProfit = 0
        print(f"{prices=}")

        while( r < len(prices)):
            nleft = prices[l]
            nright = prices[r]
            currentProfit = nright-nleft

            # buy low
            if nright < nleft:
                l=r             # set the left pointer to where right is
            # sell high
            elif currentProfit > bestProfit:
                bestProfit = currentProfit

            r += 1          # increment right pointer. Might break if at the end.
        
        return bestProfit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        

        arrayLength = len(prices)
        maxP = 0

        # Early exit solution
        if arrayLength <= 1:
            return maxP

        left, right = 0, 1

        while right < arrayLength:

            # Calculate profit? 
            
            if prices[left] < prices[right]:
                currentProfit = prices[right]-prices[left]
                maxP = max(currentProfit, maxP)
            else:
                left = right
            right += 1
        
        return maxP
