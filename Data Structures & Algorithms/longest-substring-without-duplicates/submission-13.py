class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l=0
        r=0

        max_count = 0
        seen = set()

        while r < len(s):
            while r < len(s) and s[r] not in seen:
                seen.add(s[r])
                r = r + 1  
            cur_count = r - l
            max_count = max(cur_count,max_count)
            while r < len(s) and l < len(s) and s[r] in seen:
                seen.remove(s[l])
                l = l + 1
        return max_count




            
        