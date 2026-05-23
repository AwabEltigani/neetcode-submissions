class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1 or (nums[0] == nums[1] and len(nums) == 2):
            return 1
        
        arr = nums
        arr.sort()

        l = 0
        r = 1
        maximum = 0
        

        while r < len(arr):
            currentSeq = 1
            while r < len(arr) and (arr[r] == arr[l] + 1 or arr[r]==arr[l]):
                if arr[r] == arr[l] + 1:
                    currentSeq = currentSeq + 1
                    if currentSeq > maximum:
                        maximum = currentSeq
                r = r + 1
                l = l + 1
            r = l + 1 + 1
            l = l + 1
        if currentSeq > maximum:
             maximum = currentSeq

        return maximum