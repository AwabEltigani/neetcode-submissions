class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operations = ["+","-","/","*"]
        stack = []
        

        for token in tokens:

            if token not in operations:
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                num3 = 0
                if token == "+":
                    num3 = num1 + num2
                elif token == "-":
                    num3 = num2 - num1
                elif token == "*":
                    num3 = num2 * num1
                else:
                    num3 = int(num2/num1)
                
                stack.append(num3)
        
        return stack.pop()



        