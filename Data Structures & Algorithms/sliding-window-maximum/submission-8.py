from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = deque([])
        
        # Build first window
        for i in range(k):
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            window.append(i)
        result.append(nums[window[0]])
        
        # Slide the window
        for r in range(k, len(nums)):
            # Remove elements outside current window
            if window[0] <= r - k:
                window.popleft()
            
            # Maintain decreasing order and add new element
            while window and nums[window[-1]] < nums[r]:
                window.pop()
            window.append(r)
            result.append(nums[window[0]])
        
        return result