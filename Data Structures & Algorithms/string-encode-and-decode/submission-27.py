class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_str = ""

        for word in strs:
            encoded_str += str(len(word)) + "#" + word
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        
        l = 0
        r = 0

        decoded_str = []

        while r < len(s):
            while s[r] != "#":
                r = r + 1
            steps = int(s[l:r])
            r = r + 1
            l = r
            cur_word = s[r:r+steps]
            r = r + steps
            l = r
            decoded_str.append(cur_word)

        return decoded_str



