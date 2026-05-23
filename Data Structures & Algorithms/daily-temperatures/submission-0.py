class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []

        result = [0] * (len(temperatures))

        for i,temp in enumerate(temperatures):
            if len(stack) == 0:
                stack.append([temp,i])
                continue
            while len(stack) > 0 and temp > stack[len(stack) - 1][0]:
                currentDay = stack.pop()
                result[currentDay[1]] = i - currentDay[1]
            stack.append([temp,i])
        
        return result

       