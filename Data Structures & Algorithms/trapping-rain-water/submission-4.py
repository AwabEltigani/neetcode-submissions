class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1

        while l < len(height) - 1 and height[l + 1] >=  height[l]:
            l = l + 1
        
        while r >= 0 and height[r - 1] >=  height[r]:
            r = r - 1
        
        total = 0

        maxR = height[r]#3
        minR = height[r]#3
        maxL = height[l]#2
        minL = height[l]#2

        while r > l:

            if height[l] < height[r]:
                while r > l and maxL > height[l + 1]:
                    l = l + 1
                    total += maxL - height[l]
                l = l + 1
                if len(height) - 1 < l:
                    return total
                maxL = max(height[l],maxL)
            else:
                while r > l and maxR > height[r - 1]:
                    r = r - 1
                    total += maxR - height[r]
                r = r - 1
                maxR = max(height[r],maxR)
        
        return total
                
        
        