class Solution:
    def findMin(self, nums: List[int]) -> int:
        last_item = len(nums) - 1
        
        
        l = 0
        r = len(nums) - 1

        while r > l:
            m = (r + l) // 2
            if nums[l] >= nums[r] and nums[m] >= nums[r]:
                l = m + 1
            else:
                r = m
            if l > 0 and r < last_item:
                print(l,r)
        
        return nums[l]

            
        
