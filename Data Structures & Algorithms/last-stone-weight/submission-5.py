import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        print(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones)*-1
            stone2 = heapq.heappop(stones)*-1
            res = abs(stone1-stone2)
            if res > 0:
                heapq.heappush(stones,-res)

        return 0 if len(stones) == 0 else stones[0]*-1