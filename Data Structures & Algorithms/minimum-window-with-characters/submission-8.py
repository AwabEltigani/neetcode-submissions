class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): #if t is greater than s then there is no s that contains t
            return ""
        
        s1CharCount = {}

        for c in t:
            s1CharCount[c] = s1CharCount.get(c,0)+1#creates the hashmap of where the keys are the characters and the values are their frequencies
        
        l = 0
        r = 0
        
        if l == len(t):
            return ""

        

        shortestString = ""

        s2CharCounter = {}
        matches = 0

        while r < len(s):

           
            
                
            while r < len(s) and matches != len(s1CharCount):
                
                if s[r] in s1CharCount:
                    s2CharCounter[s[r]] = s2CharCounter.get(s[r],0)+1
                    if s2CharCounter.get(s[r],0) == s1CharCount.get(s[r],0):
                        matches += 1
                
                
                
                r = r + 1
            
            
            while matches == len(s1CharCount):
                if shortestString == "" or len(shortestString) > len(s[l:r]):
                    shortestString = s[l:r]
                if s[l] in s1CharCount:
                    s2CharCounter[s[l]] = s2CharCounter.get(s[l]) - 1
                    if s1CharCount.get(s[l]) > s2CharCounter.get(s[l]):
                        matches -= 1

                l = l + 1
            
            
        
        
            
            
            
        
        return shortestString
            
            
            

    
            

            


