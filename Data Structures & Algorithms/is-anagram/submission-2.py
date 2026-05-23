class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_count={}
        t_count={}

        for char in s:
            if char in s_count.keys():
                s_count[char] = s_count.get(char) + 1
            else:
                s_count[char] = 1

        
        for char in t:
            if char in t_count.keys():
                t_count[char] = t_count.get(char) + 1
            else:
                t_count[char] = 1
        
        if len(s_count) != len(t_count):
            return False
        
        for char in s:
            if s_count.get(char) != t_count.get(char,0):
                return False
        
        return True
                
        