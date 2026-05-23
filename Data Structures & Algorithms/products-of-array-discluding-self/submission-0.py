class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        arr : List[int] = []
        total : int = nums[0]
        arr.append(1)
        
 

        for i in range(1,len(nums)):
                arr.append(total)
                total *= nums[i]
        
        total = 1

        for j in range(len(nums) - 1,-1,-1):
            arr[j] *= total
            total *= nums[j] 
        

        return arr

        


        