class Solution:

    def encode(self, strs: List[str]) -> str:

        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word
        
        return result

    def decode(self, s: str) -> List[str]:


        l = 0
        r = 0
        res = []

        while r < len(s):
            while r < len(s) and s[r] != "#":
                r = r + 1

            lengthOfWord = int(s[l:r])
            
            word = ""

            for num in range(r + 1 , r + 1 + lengthOfWord):
                word += s[num]
            
            res.append(word)

            l = r + 1 + lengthOfWord
            r = r + 1 + lengthOfWord
        
        return res

        


        
