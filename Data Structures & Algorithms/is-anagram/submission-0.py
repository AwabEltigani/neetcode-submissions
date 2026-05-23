class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if(len(s) != len(t)):
            return False
        
        s_hash = {}
        t_hash = {}

        for char in s:
            if char not in s_hash:
                s_hash[char] = 1
            else:
                s_hash[char] += 1

        for char in t:
            if char not in t_hash:
                t_hash[char] = 1
            else:
                t_hash[char] += 1
        
        for key in s_hash.keys():
            if s_hash.get(key) != t_hash.get(key):
                return False

        return True
