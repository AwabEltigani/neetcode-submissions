class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap : dict = {}
        result : List = []

        for num in nums:
            freq = hashmap.get(num,0) + 1
            hashmap[num] = freq
        
        

        buckets = buckets = [[] for _ in range(len(nums)+1)]

        

        for key,value in hashmap.items():
            buckets[value].append(key)


        for i in range(len(buckets) - 1,0,-1):
                for num in buckets[i]:
                    if k > len(result):
                        result.append(num)
        
        return result


