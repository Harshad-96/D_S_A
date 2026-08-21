class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        # Your Code Goes Here
        import heapq
        heapq.heapify(sticks)
        ans = 0
        while len(sticks) > 1:
            summ = heapq.heappop(sticks) + heapq.heappop(sticks)
            ans += summ
            heapq.heappush(sticks,summ)
        return ans
        