class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []
        left_sum = 1

        #all the numbers to the left
        for num in nums:
            result.append(left_sum)
            left_sum *= num
        
        #all the numbers to the right
        right_sum = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= right_sum
            right_sum *= nums[i]
        
        return result
        
        