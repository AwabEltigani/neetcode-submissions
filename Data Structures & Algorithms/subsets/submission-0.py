class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        
        res = []
        max_len = len(nums)

        def getsubsets(arr,index,max_len):

            
            res.append(arr)
        

            while index < max_len:
                arr.append(nums[index])
                arr_copy = arr.copy()
                getsubsets(arr_copy,index + 1,max_len)
                index += 1
                arr.pop()
                
                
            
        
        getsubsets([],0,len(nums))

        return res



        