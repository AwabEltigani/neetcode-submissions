import heapq,math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        closest_points = [(math.sqrt(point[0]*point[0]+point[1]*point[1]),i) for i,point in enumerate(points)]

        heapq.heapify(closest_points)
        print(closest_points)
        res = []


        for i in range(k):
            cur_point = heapq.heappop(closest_points)
            res.append(points[cur_point[1]])

        return res
        
        
        


        
        