class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operations = ("+","-","*","/")
        if len(tokens) == 1:
            return int(tokens[0])

        for i in range(len(tokens)):
            if tokens[i] in operations:
                curSum = 0
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                
                if tokens[i] == "+":
                    curSum = num1 + num2
                elif tokens[i] == "-":
                    curSum = num1 - num2
                elif tokens[i] == "/":
                    curSum = int(num1/num2)
                else:
                    curSum = num1*num2
                stack.append(curSum)
                
            else:
                stack.append(tokens[i])
        
        return stack.pop()