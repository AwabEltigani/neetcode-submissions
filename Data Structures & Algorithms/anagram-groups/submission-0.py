class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 1:
            return [strs]

        hashmap : dict = {}
        result : List = [];
        

        for word in strs:
            currentWord : dict = {};
            for char in word:
                currentWord[char] = currentWord.get(char, 0) + 1

            key = tuple(sorted(currentWord.items()));
            
            if key not in hashmap:
                hashmap[key] = [word]      
            else:
                hashmap[key].append(word)   
            
        result = [arr for arr in hashmap.values()]
    
        

    
        return result
        




        