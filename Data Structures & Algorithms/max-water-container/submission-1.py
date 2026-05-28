class Solution:
    def maxArea(self, heights: List[int]) -> int:
         maxArea = 0
         l = 0
         r = len(heights) - 1

         while r > l:
            curArea = (r-l) * min(heights[l],heights[r])
            maxArea = max(curArea,maxArea)
            if heights[l] > heights[r]:
                r = r - 1
            else:
                l = l + 1
            
         return maxArea