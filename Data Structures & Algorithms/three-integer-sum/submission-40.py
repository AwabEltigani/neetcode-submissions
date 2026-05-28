class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        
        for cur in range(len(nums) - 2):
            # Skip duplicate values for cur
            if cur > 0 and nums[cur] == nums[cur - 1]:
                continue
            
            l = cur + 1
            r = len(nums) - 1
            
            while r > l:
                total = nums[cur] + nums[l] + nums[r]
                
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    triplets.append([nums[cur], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicates AFTER moving both pointers
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                    while r > l and nums[l] == nums[l - 1]:
                        l += 1
        
        return triplets