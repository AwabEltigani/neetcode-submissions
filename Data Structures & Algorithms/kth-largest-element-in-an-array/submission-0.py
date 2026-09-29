import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        new_k = len(nums) - k

        heapq.heapify(nums)

        for i in range(new_k):
            heapq.heappop(nums)
        
        return nums[0]