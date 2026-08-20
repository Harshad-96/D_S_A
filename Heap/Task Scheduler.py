import deque
import Counter


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        import heapq
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        cooldown = deque()  # stores [count, available_time]
        
        while maxHeap or cooldown:
            time += 1
            
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1  
                if cnt < 0:
                    cooldown.append([cnt, time + n])
            
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(maxHeap, cooldown.popleft()[0])
        
        return time