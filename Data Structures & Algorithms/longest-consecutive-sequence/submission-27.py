class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        non_dupes = set(nums)
        max_seq = 0


        for num in non_dupes:
            cur_seq = 1
            if num - 1 not in non_dupes:
                while num + 1 in non_dupes:
                    cur_seq = cur_seq + 1
                    num = num + 1
                max_seq = max(max_seq,cur_seq)
        
        return max_seq
                