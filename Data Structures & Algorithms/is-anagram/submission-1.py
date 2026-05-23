class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if(len(s) != len(t)):
            return False

        alphaCountS : dict = {}
        alphaCountT : dict = {}

        for char in s:
            if char in alphaCountS:
                alphaCountS.update({char : alphaCountS.get(char) + 1})
            else:
                alphaCountS.update({char:1})
        
        for char in t:
            if char in alphaCountT:
                alphaCountT.update({char : alphaCountT.get(char) + 1})
            else:
                alphaCountT.update({char:1})
        
        for char in alphaCountS.keys():
            if(alphaCountS.get(char) != alphaCountT.get(char)):
                return False
        

        return True

        
        