from collections import deque 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        result = []
        window = deque([nums[0]])

        currentMax = nums[0]

        for i in range(1,k):
            if nums[i] > currentMax:
                currentMax = nums[i] 
            window.append(nums[i])
        
        result.append(currentMax)

        r = k - 1
        l = 0

        while r < len(nums):
            poppedLeft = window.popleft()
            l = l + 1
            r = r + 1

            if r >= len(nums):
                break

            window.append(nums[r])

            if poppedLeft == currentMax:
                currentMax = nums[l]
                for i in range(l + 1,r + 1):
                    if nums[i] > currentMax:
                        currentMax = nums[i]
            else:
                if nums[r] > currentMax:
                    currentMax = nums[r]
            
            result.append(currentMax)
        
        return result
                    
            




        
        