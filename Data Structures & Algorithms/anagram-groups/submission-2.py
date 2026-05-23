class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groupedValues = {}


        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            if tuple(count) in groupedValues:
                arr = groupedValues.get(tuple(count))
                arr.append(word)
                groupedValues[tuple(count)] = arr
            else:
                groupedValues[tuple(count)] = [word]
            
            
        return list(groupedValues.values())
