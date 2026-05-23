class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxBananas = 0
        if len(piles) == h:
            for pile in piles:
                maxBananas = max(pile,maxBananas)
            return maxBananas
        
        for pile in piles:
            maxBananas = max(pile,maxBananas)
        
        r = maxBananas
        l = 1
        currentTime = 0
        finalRate = 1000000000000000
        
        while r >= l:
            currentTime = 0
            curRate = math.floor((r+l)/2)
            for pile in piles:
                if pile <= curRate:
                    currentTime += 1
                else:
                    currentTime += math.ceil(pile / curRate)
            if currentTime == h:
                finalRate = min(curRate,finalRate)
                r = curRate - 1
            elif currentTime < h:
                finalRate = min(curRate,finalRate)
                r = curRate - 1
            else:
                l = curRate + 1

        return finalRate
            

        
                

            
            


        



        #[1,4,3,2] h = 9
