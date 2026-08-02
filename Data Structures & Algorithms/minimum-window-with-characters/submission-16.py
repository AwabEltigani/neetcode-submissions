class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == 0 or len(t) == 0:
            return ""
        if len(t) > len(s):
            return ""
        if s == t:
            return s
        
        seen_s = Counter()
        seen_t = Counter()
        l = 0
        r = 0
        min_count = float("inf")
        res = ""

        for char in t:
            seen_t[char]+=1
        
        counter = 0
        
        while l < len(s):
            if s[l] in seen_t:
                while r < len(s) and counter < len(seen_t):
                    
                    if s[r] in seen_t:
                        seen_s[s[r]] += 1
                        if seen_s.get(s[r]) == seen_t.get(s[r]):
                            counter += 1
                    r = r + 1
              
                
                condition = True

                for char in seen_t.keys():
                    if seen_t.get(char) > seen_s.get(char):
                        condition = False
                        break

                if condition:
                    print(s[l:r],res,min_count,r-l+1)
                    count = r - l + 1
                    
                    if min_count > count:
                        min_count = count
                        res = s[l:r]
                seen_s[s[l]] = seen_s.get(s[l]) - 1
                if seen_s.get(s[l]) < seen_t.get(s[l]):
                    counter -= 1


                while l<len(s) and s[l] not in seen_t:
                    l = l + 1

                l = l + 1
            else:
                l = l + 1
        

        return res