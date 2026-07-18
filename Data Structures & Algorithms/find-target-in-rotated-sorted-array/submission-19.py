class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        """
        [6,1,2,3,4,5] -> [6,1,2] [3,4,5] target 1 -> t > or < m r = r - 1
        if left > right -> that means that this side is unsorted 
        we keep checking with the algothrim that we create 
        if right > left -> that means that this side is sorted 
        we can do binary search
        [6,1,2,3,4,5] -> l = 6 m = 2 r = 5 t = 1
        m > t -> l > r or r > l -> binary search or keep elimating the pool 
        """

        l = 0
        r = len(nums) - 1

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        while r > l:
            m = (r + l) // 2
            if nums[l] == target:
                return l
            if nums[r] == target :
                return r
            if nums[m] == target:
                return m
            if target > nums[m]:
                if nums[l] > nums[m]:
                    l =l+1
                else:
                    r=r-1
            else:
                if nums[r] > nums[m]:
                    l = l + 1
                else:
                    l = l + 1 
        
        return -1