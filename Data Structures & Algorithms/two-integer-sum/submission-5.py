class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        pairs = {}

        for i,num in enumerate(nums):
            result = target - num #3
            if result in pairs.keys():
                return [pairs.get(result),i]
            pairs[num] = i
        
