class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        maxArea = 0
        curArea = 0
        currentI = 0

        for i in range(len(heights)):
            currentI = i
            if i == 0 or len(stack)==0:
                stack.append([heights[i],i])
                continue
            while len(stack) > 0 and stack[len(stack) - 1][0] > heights[i]:
                curHeight = stack.pop()
                curArea = curHeight[0] * (i - curHeight[1])
                maxArea = max(curArea,maxArea)
                currentI = curHeight[1]
            stack.append([heights[i],currentI])
        
        while len(stack) > 0:
            curHeight = stack.pop()
            curArea = curHeight[0] * (len(heights) - curHeight[1])
            maxArea = max(curArea,maxArea)
        return maxArea