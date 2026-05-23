class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        arrs = [[] for _ in range(len(nums) + 1)]
        
       
        
        

        counter = {}

        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
        
        for key,value in counter.items():
            arrs[value].append(key)
        

        r = len(arrs) - 1
        i = 0

        res = []

        while(r >= 0 ):
            for num in arrs[r]:
                if(k > 0):
                    res.append(num)
                    k = k-1
            r = r - 1
                
        


        
        
        return res
        