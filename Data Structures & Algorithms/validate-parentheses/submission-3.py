class Solution:
    def isValid(self, s: str) -> bool:
        
        validPairs = {
            "(":")",
            "[":"]",
            "{":"}"
        }

        validString = ""
        for char in s:
            if char in validPairs.keys():
                validString += char
            else:
                if len(validString) == 0:
                    return False
                lastChar = validString[-1]
                if validPairs.get(lastChar) == char:
                    validString = validString[0:-1]
                else:
                    return False
        
        if len(validString) != 0:
            return False
        else:
            return True

