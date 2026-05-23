class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [0] * len(nums)
        currentProduct = 1
        for i,num in enumerate(nums):
            if i == 0:
                res[i] = currentProduct
                currentProduct *= nums[i]
            else:
                res[i] = currentProduct
                currentProduct *= nums[i]
        
        currentProduct = 1

        for i in range(len(nums) - 1 , -1 , -1):
            if i == len(nums) - 1:
                res[i] *= currentProduct
                currentProduct *= nums[i]
            else:
                res[i] *= currentProduct
                currentProduct *= nums[i]
                

        return res
        
