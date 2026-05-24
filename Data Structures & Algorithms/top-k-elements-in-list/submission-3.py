class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = {}

        for num in nums:
            if num in freq_map.keys():
                freq_map[num] = freq_map.get(num) + 1
            else:
                freq_map[num] = 1
        
        freq_arr = [[] for _ in range(len(nums) + 1)]

        for key,value in freq_map.items():
            freq_arr[value].append(key)
        
        solution_arr = []

        for i in range(len(freq_arr) - 1,-1,-1):
            if len(freq_arr[i]) == 0:
                continue
            if len(solution_arr) >= k:
                break
            
            for num in freq_arr[i]:
                solution_arr.append(num)

        return solution_arr
        