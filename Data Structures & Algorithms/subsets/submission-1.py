class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        
        res = []
        max_len = len(nums)
        arr = []

        def getsubsets(index):
            print(arr.copy())
            if index >= max_len:
                res.append(arr.copy())
                return
            
            
            arr.append(nums[index])
            getsubsets(index + 1)

            arr.pop()
            getsubsets(index + 1)
            
        
        getsubsets(0)

        return res



        