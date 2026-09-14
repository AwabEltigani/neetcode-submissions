class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res =[]
        

        def dfs(arr,index,total):
            if total == target:
                res.append(arr.copy())
                return
            if total > target:
                return

            for i in range(index,len(nums)):
                arr.append(nums[i])
                total = total + nums[i]
                dfs(arr,i,total)
                total -= nums[i]
                arr.pop()
        dfs([],0,0)
        return res





