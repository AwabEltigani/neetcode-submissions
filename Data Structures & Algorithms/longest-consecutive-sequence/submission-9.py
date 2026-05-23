class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        if len(nums) == 1 or (nums[0] == nums[1] and len(nums) == 2):
            return 1
        
        nums_set = set(nums)

        #[2,20,4,10,3,5]
        
        maxSeq = 0

        for i in range(len(nums)):
            curSeq = 1
            current = nums[i]
            while current in nums_set:
                curSeq = curSeq + 1
                current = current + 1
                if curSeq > maxSeq:
                    maxSeq = curSeq
        
        return maxSeq - 1

