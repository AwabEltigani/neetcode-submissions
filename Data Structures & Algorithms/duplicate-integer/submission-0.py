class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        non_dupes = set();

        for num in nums:
            if num in non_dupes:
                return True
            non_dupes.add(num);
        
        return False;