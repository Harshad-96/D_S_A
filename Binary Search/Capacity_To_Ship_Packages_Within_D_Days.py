class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low+high)//2
            if self.need_day(weights,mid) <= days:
                high = mid - 1
            else:
                low = mid + 1
        return low
            


    def need_day(self,weights,capacity):
        n = len(weights)
        day = 1 
        load  = 0
        for i in range(n):
            if load + weights[i] > capacity:
                day += 1
                load = weights[i]
            else:
                load += weights[i]
        return day
        