class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1
        maxArea = 0
        area = 0

        while r >= l:
            if heights[r] < heights[l]:
                area = (r - l) * heights[r]
                r = r - 1
            else:
                area = (r - l) * heights[l]
                l = l + 1

            maxArea = max(maxArea,area)
        
        return maxArea
