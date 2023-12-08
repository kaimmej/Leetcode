class Solution:
    def kokoEat(self, k: int, piles: List[int]) -> int:
        hours = 0
        for bananas in piles:
            hours += math.ceil(bananas / k)

        return hours



    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPiles = max(piles)


        # binary serach koko eats using the k-value array
        left = 1
        right = max(piles)
        result = right

        while left <= right:
            mid = (right+left)//2
            current_kokoEats = self.kokoEat(mid, piles)

            
            # if it took MORE TIME (h=8 but koko took h=10...)
            if current_kokoEats <= h:
                # then we must increase k.. so binary search moves right. 
                result = min(result, mid)
                right = mid-1

            # if it took LESS TIME (h=8 but koko took h=5...)
            else:
                left = mid+1



        return result