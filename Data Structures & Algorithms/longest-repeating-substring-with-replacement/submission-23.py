class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        r = 0
        char_count = Counter()
        most_frequent = 0
        longest_string = 0

        for r in range(len(s)):
            char_count[s[r]] += 1
            most_freq = char_count.most_common(1)[0][1]
            while l < r and ((r - l + 1) - most_freq - k) > 0:
                char_count[s[l]] -= 1
                most_freq = char_count.most_common(1)[0][1]
                l = l + 1
            longest_string = max(longest_string,r-l+1)
    # 1. add s[r] to char_count
    # 2. update most_frequent (just compare against char_count[s[r]])
    # 3. while window is invalid: shrink from l
    # 4. update longest_string
        return longest_string

