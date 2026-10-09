import heapq
from collections import deque,Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        cooldown_time = deque([])
        running_priority = []

        frequency = Counter(tasks)

        for _,val in frequency.items():
            running_priority.append(-val)
        
        heapq.heapify(running_priority)
        total_time = 0

        while running_priority or cooldown_time:
            if len(cooldown_time) > 0:
                task,time_start = cooldown_time[0]
                time_spent = total_time - time_start
                if time_spent == n + 1:
                    cooldown_time.popleft()
                    heapq.heappush(running_priority,-task)
            
            if len(running_priority) > 0:
                top = abs(heapq.heappop(running_priority))
                top -= 1
                if top > 0:
                    cooldown_time.append([top,total_time])
            
            total_time += 1
        
        return total_time














                


