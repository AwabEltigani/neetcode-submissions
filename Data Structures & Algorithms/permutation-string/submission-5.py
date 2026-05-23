class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1Count = {}

        for char in s1:
            s1Count[char] = s1Count.get(char,0) + 1
        
        s2Count = {}

        l = 0
        
        while l < len(s2) and s2[l] not in s1Count.keys():
            l = l + 1
        
        
        r = l

        while r < len(s2):

            while r < len(s2) and s2[r] not in s1Count.keys():
                l = l + 1
                r = l
                s2Count = {}

            

            if r < len(s2) and s2[r] in s1Count.keys() and s1Count.get(s2[r],0) > s2Count.get(s2[r],0):
                s2Count[s2[r]] = s2Count.get(s2[r],0) + 1
                r = r + 1
            else:
                while l < len(s2) and s1Count.get(s2[r],0) <= s2Count.get(s2[r],0):
                    if s2Count.get(s2[l],0) - 1 <= 0:
                        s2Count.pop(s2[l],0)
                    else:
                        s2Count[s2[l]] = s2Count.get(s2[l],0) - 1
                    l = l + 1
            if len(s1Count) == len(s2Count):
                for i,key in enumerate(s2Count.keys()):
                    if i == len(s2Count) - 1 and s2Count.get(key) == s1Count.get(key):
                        return True
                    elif s2Count.get(key) != s1Count.get(key):
                        break
                    else:
                        break
                
            if len(s1Count) == len(s2Count):
                if s1Count == s2Count:
                    return True
                    
                
            
            
        
        return False
                


