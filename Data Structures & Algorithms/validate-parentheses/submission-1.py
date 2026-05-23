class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        combinations = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        for i in range(len(s)):
            if s[i] in combinations.keys():
                stack.append(s[i])
            else:
                currentItem = ""
                if i > - 1 and len(stack) > 0:
                    currentItem = stack.pop()
                if combinations.get(currentItem) != s[i]:
                    return False
        
        if len(stack) != 0:
            return False

        
        return True