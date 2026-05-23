class Solution:
    def search(self, nums: List[int], target: int) -> int:

        
        
        l = 0
        r = len(nums) - 1

        while(r > l):
            mid  = (r+l)//2

            if nums[mid] == target:
                return mid
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            
            if nums[l] <= nums[mid] and target >= nums[l] and nums[mid] >= target: #everything on the left is sorted
                if nums[l] == target:
                    return l
                if nums[r] == target:
                    return r
                r = mid - 1
            elif nums[mid] < nums[r] and target <= nums[r] and nums[mid] < target:
                l = mid + 1
            elif nums[l] > nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        
        if nums[l] == target:
            return l
        

        return -1