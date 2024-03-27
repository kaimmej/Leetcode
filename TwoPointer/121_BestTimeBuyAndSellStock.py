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