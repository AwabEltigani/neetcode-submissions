class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        minimum_num = 100000000000000

        l = 0
        r = len(nums)-1

        if nums[l] < nums[r]:
            return nums[l]

        while r >= l:
            m = (l + r) // 2
            if r == l:
                return nums[l]
            
            if nums[m] > nums[l] and nums[m] > nums[r]:
                l = m + 1
            elif nums[m] > nums[l] and nums[r] > nums[m]:
                r = m - 1
            elif nums[l] >= nums[m] and nums[m] <= nums[r]:
                if len(nums) > 2 and nums[m - 1] > nums[m] and nums[m + 1] > nums[m]:
                    return nums[m]
                elif len(nums) == 2:
                    if m == 0 and nums[m + 1] >= nums[m]:
                        return nums[m]
                    else:
                        return nums[m + 1]
                else:
                    r = m - 1
            else:
                l = r
                        