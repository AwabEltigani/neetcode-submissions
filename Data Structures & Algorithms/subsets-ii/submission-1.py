class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        data = []
        prev = -1
        def dfs(index):
     
            if index > len(nums):
                return
            
            res.append(data.copy())
            prev = float("-inf")
            for i in range(index,len(nums)):
                if nums[i] != prev:
                    data.append(nums[i])
                    dfs(i+1)
                    data.pop()
                    prev = nums[i]
                    
                
        dfs(0)
        return res
