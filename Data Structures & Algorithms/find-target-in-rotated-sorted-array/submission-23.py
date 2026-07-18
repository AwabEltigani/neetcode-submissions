class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        while r > l:
            m = (r + l) // 2
            if nums[l] == target:
                return l
            if nums[r] == target :
                return r
            if nums[m] == target:
                return m
            if target > nums[m]:
                if nums[l] > nums[m]:#elimiates the check of the left side since target > m and l > target meaning that target greater than both left and target
                    l =l+1
                else:
                    r=r-1
            else:
                l = l + 1
        
        return -1