class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1
        area = 0

        while r > l and height[l] < height[l + 1]:
            l = l + 1
        
        
        while r > l and height[r] < height[r - 1]:
            r = r - 1
        
        maxLeftBar = [height[l],l]
        maxRightBar = [height[r],r]

        while r > l:
            while r > l and maxLeftBar[0] > height[l + 1]:
                l = l + 1
            if l < r:
                l = l+1
            if height[l] >= maxLeftBar[0]:
                for i in range(maxLeftBar[1] + 1,l):
                    area += maxLeftBar[0] - height[i]
                maxLeftBar = [height[l],l]
            else:
                for i in range(maxLeftBar[1] + 1,l):
                    if height[i] > height[l]:
                        continue
                    area += height[l] - height[i]
            
            # while r > l and height[r] > height[r - 1]:
            #     r = r - 1
            # r = r - 1
            # if height[r] >= maxRightBar[0]:
            #     for i in range(maxRightBar[1] + 1,r):
            #         area += maxRightBar[0] - height[r]
            #     maxRightBar = [height[r],r]
            # else:
            #     for i in range(maxRightBar[1],r):
            #         area = height[r] - height[i]

            
        
        return area

