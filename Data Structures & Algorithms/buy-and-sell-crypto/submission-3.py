class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        max_profit = 0
        if len(nums) == 1 or len(nums) == 0:
            return max_profit

        start = nums[0]
        

        for i in range(1,len(nums)):
            if nums[i] < start:
                start = nums[i]
            else:
                max_profit = max(nums[i] - start,max_profit)
            

        return max_profit