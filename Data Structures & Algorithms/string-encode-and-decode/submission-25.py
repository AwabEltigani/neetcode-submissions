class Solution:

    def encode(self, strs: List[str]) -> str:
        string : str = ""
        for word in strs:
            string += str(len(word)) + "#"+ word
        
        return string

    def decode(self, s: str) -> List[str]:
        l : int = 0
        r : int = 0
        arr : List[str] = []

        

        while(r < len(s)):

            while r < len(s) and s[r] != "#":
                r = r + 1
        
        
            num = int(s[l:r])

            word = s[r + 1:r + num + 1]

            arr.append(word)
            
            l = num + 1 + r
            r = num + 1 + r


        return arr
        
    

       
            

            

