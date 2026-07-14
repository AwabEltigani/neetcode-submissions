class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        max_pile = 0

        for pile in piles:
            if max_pile < pile:
                max_pile = pile
        
        min_k = 1
        max_k = max_pile
        minimum_rate = 1000000000000000
        while min_k <= max_k:
            hours = 0
            mid_k = (min_k + max_k)//2
            for pile in piles:
                hours += math.ceil(pile/mid_k)
            if hours > h:
                min_k = mid_k + 1
            else:
                if minimum_rate > mid_k:
                    minimum_rate = mid_k
                max_k = mid_k - 1
        
        return minimum_rate
            