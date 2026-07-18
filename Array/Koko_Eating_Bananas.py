import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low = 1
        high = max(piles)
        ans = float('inf')
        while low <= high:
            mid = (low+high)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/float(mid)) 
            if hours <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
        