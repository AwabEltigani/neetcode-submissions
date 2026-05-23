class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while k > j:
                if nums[i]+nums[j]+nums[k] == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    j = j + 1
                    k = k - 1
                    while k > j and j > 0 and nums[j] == nums[j - 1]:
                        j = j + 1
                    
                elif nums[i]+nums[j]+nums[k] > 0:
                    k = k - 1
                else:
                    j = j + 1
        
        return res