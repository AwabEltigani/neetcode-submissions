class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) == 0:
            return True

        if len(s2) < len(s1) or len(s2) == 0:
            return False
        
        s1_counter = Counter()
        
        for s in s1:
            if s in s1_counter:
                s1_counter[s] += 1
            else:
                s1_counter[s] = 1
        
        s2_counter = Counter()

        for l in range(len(s2)):
            if s2[l] in s1_counter:
                r = l
                while r < len(s2) and s2[r] in s1_counter and s1_counter != s2_counter:
                    if s2[r] in s2_counter:
                        s2_counter[s2[r]] += 1
                    else:
                        s2_counter[s2[r]] = 1
                    r = r + 1

                if s1_counter == s2_counter:
                    return True
                else:
                    s2_counter = Counter()
            
        return False