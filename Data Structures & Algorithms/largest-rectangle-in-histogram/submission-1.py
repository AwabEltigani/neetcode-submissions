class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []

        max_area = 0
        for i,height in enumerate(heights):
            last_height = 0
            if len(stack) == 0:
                stack.append([i,height])
                continue
            
            while len(stack) > 0 and height < stack[-1][1]:
                last_height = stack.pop()
                area = last_height[1] * (i-last_height[0])
                max_area = max(max_area,area)
            
            stack.append([last_height[0] if last_height else i,height])
        
        while len(stack) > 0:
            last_height = stack.pop()
            area = last_height[1] * (len(heights) - last_height[0])
            max_area = max(max_area,area)
        
        return max_area
            

