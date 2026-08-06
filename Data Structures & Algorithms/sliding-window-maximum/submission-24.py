from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        l = 0
        r = k 
        res = []
        max_value_queue = deque()
        max_value = float("-infinity")
        if k == 1:
            return nums

        
        #O(n)
        for i in range(k - 1,len(nums)):
            if i == k - 1:
                for j in range(k):
                    
                    if len(max_value_queue)== 0:
                        max_value_queue.append(j)
                        continue
                    while len(max_value_queue) > 0 and nums[max_value_queue[- 1]] < nums[j]:
                        max_value_queue.pop()
                        
                    max_value_queue.append(j)
                res.append(nums[max_value_queue[0]])
            else:
                
                while len(max_value_queue) > 0 and nums[max_value_queue[- 1]] < nums[i]:
                    max_value_queue.pop()

                max_value_queue.append(i)

                if i - k == max_value_queue[0]:
                    max_value_queue.popleft()
                
                res.append(nums[max_value_queue[0]])
                print(max_value_queue[0],nums[i - k])
                
                
                
                
                
         
                
                        
        return res

                
            


        