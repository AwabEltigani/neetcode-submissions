class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return nums[1]
            else:
                return nums[0]
        
        while r > l:
            mid = math.floor((l+r)/2)
            if l <len(nums)-1 and r >= 0  and nums[mid - 1] > nums[mid] < nums[mid + 1]:
                return nums[mid]
            else:
                if nums[mid] < nums[r]:
                    
                    r = mid - 1
                else:
                    l = mid + 1
        
        return nums[l]
        
        