class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #nums[i] + nums[j] == target
        #target - nums[i] = nums[j]
        #
        #
        #
        #
        #
        #
        #

        pair = {}
  

        for i in range(len(nums)):
            num = target - nums[i];
            if(num in pair.keys()):
                return [pair.get(num),i]
            else:
                pair[nums[i]] = i

        

        

            