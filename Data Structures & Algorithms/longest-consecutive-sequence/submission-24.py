class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        if len(nums) == 1 or (nums[0] == nums[1] and len(nums) == 2):
            return 1
        
        nums_set = set(nums)

        #[2,20,4,10,3,5]
        
        maxSeq = 0
        l = 0
        r = 0
        start = -10000000
        currentNum = 0
        curSeq = 0

        for num in nums:

            if num - 1 not in nums_set:
                curSeq = 1
                currentNum = num
            
                while (currentNum + 1) in nums_set:
                    curSeq += 1
                    currentNum = currentNum + 1
                    if curSeq > maxSeq:
                        maxSeq = curSeq
            
           

        

        return maxSeq
                


