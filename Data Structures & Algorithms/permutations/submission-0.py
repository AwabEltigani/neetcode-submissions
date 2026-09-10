class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def dfs(seen,arr):
            if len(arr) == len(nums):
                res.append(arr.copy())
                return
            
            for num in nums:
                if num not in arr:
                    arr.append(num)
                    seen.add(num)
                    dfs(seen,arr)
                    arr.pop()
                    seen.remove(num)
        
        dfs(set(),[])

        return res


        