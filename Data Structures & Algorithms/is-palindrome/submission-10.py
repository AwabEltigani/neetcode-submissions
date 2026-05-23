class Solution:
    def isPalindrome(self, s: str) -> bool:

        lower_s = s.lower()
        l = 0
        r = len(s) - 1

        while r > l:
            while r > l and not lower_s[r].isalnum():
                r = r - 1
            
            while r > l and not lower_s[l].isalnum():
                l = l + 1
            
            if lower_s[r] != lower_s[l]:
                return False
            
            r = r - 1
            l = l + 1

        
        return True

        