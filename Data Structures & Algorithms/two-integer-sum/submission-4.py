class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numbers = {}
        
        for i,num in enumerate(nums):
            value = target - num
            if value in numbers:
                return [numbers.get(value),i]
            numbers.update({num:i})


        