import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        while len(nums) > k:
            print(1)
            heapq.heappop(nums)
        self.heap = nums
        self.k = k

    def add(self, val: int) -> int:
        if len(self.heap) == self.k:
            if  val > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap,val)
        else:
            heapq.heappush(self.heap,val)
        
        print(self.heap)
        return self.heap[0]
        
