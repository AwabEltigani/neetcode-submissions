class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        result = [0]*len(temperatures)
        
        for i,temp in enumerate(temperatures):
            cur_temp = [temp,i]
            if len(stack) == 0:
                stack.append(cur_temp)
                continue
            if len(stack) == 0 and cur_temp[0] < stack[-1][0]:
                stack.append(cur_temp)
            else:
                while len(stack) > 0 and cur_temp[0] > stack[-1][0]:
                    top = stack.pop()
                    diff_days = top[1]
                    result[top[1]]=(i - diff_days)
                stack.append(cur_temp)
        
        return result





            
                
            
        


        