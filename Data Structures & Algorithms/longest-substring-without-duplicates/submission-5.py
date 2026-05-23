class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        l = 0
        r = 1
        maxSequence = 0
        curSeq = 0
        currentItems = set()
        currentItems.add(s[l])

        while r < len(s):
            while r < len(s) and s[r] not in currentItems:
                currentItems.add(s[r])
                r = r + 1
            curSeq = (r - l)
            maxSequence = max(maxSequence,curSeq)
            while r < len(s) and s[r] in currentItems:
                currentItems.remove(s[l])
                l = l + 1
            
        
        return maxSequence

