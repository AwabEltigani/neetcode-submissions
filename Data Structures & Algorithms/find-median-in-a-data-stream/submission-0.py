import heapq
class MedianFinder:

    def __init__(self):
        self.left_side = []
        self.right_side = []
        self.total_elements = 0

    def addNum(self, num: int) -> None:

        if self.total_elements == 0:
            heapq.heappush(self.left_side,-num)
        else:
            if len(self.left_side) > len(self.right_side):
                if -self.left_side[0] > num:
                    last_element = -heapq.heappop(self.left_side)
                    heapq.heappush(self.left_side,-num)
                    heapq.heappush(self.right_side,last_element)
                else:
                    heapq.heappush(self.right_side,num)
            else:
                if num > self.right_side[0]:
                    last_element = heapq.heappop(self.right_side)
                    heapq.heappush(self.left_side,-last_element)
                    heapq.heappush(self.right_side,num)
                else:
                    heapq.heappush(self.left_side,-num)
        
        self.total_elements += 1


    def findMedian(self) -> float:
        if self.total_elements % 2 == 0:
            return (-self.left_side[0] + self.right_side[0]) / 2
        else:
            return -self.left_side[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()