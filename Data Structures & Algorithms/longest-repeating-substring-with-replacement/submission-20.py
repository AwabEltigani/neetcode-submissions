class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        r = 0

        maxSequence = 0
        counter = {}

        def getMostRepeatedChar(counter : dict):
            maxCount = 0

            if len(counter) == 0:
                return maxCount

            for value in counter.values():
                if value > maxCount:
                    maxCount = value
            
            return maxCount

        for r in range(len(s)):
            maxCount = getMostRepeatedChar(counter)
                
            counter[s[r]] = counter.get(s[r], 0) + 1
            maxCount = getMostRepeatedChar(counter)

            while (r - l + 1) - maxCount > k:

                counter[s[l]] = counter.get(s[l],0) - 1
                if counter.get(s[l],0) <= 0:
                    counter.pop(s[l])
    
                l = l + 1

                maxCount = getMostRepeatedChar(counter)

            maxSequence = max(maxSequence,r - l + 1)
        
        return maxSequence
        

        
        

                

                

    







    

