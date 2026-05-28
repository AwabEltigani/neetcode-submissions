class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s) - 1

        s = s.lower()

        while r > l:
            while r > l and not s[r].isalpha() and not s[r].isdigit():
                r = r - 1
            while r > l and not s[l].isalpha() and not s[l].isdigit():
                l = l + 1

            if s[l] != s[r]:
                return False
            
            l = l + 1
            r = r - 1
        
        return True
            