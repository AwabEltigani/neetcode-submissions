class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_map = {}

        for word in strs:
            char_count={}
            for char in word:
                if char in char_count.keys():
                    char_count[char] = char_count.get(char) + 1
                else:
                    char_count[char] = 1
            char_tuple = tuple(sorted(word))
            if char_tuple in anagram_map.keys():
                anagram_map[char_tuple].append(word)
            else:
                anagram_map[char_tuple] = [word]

        
        return list(anagram_map.values())

        
            

        
            
        

        
            

