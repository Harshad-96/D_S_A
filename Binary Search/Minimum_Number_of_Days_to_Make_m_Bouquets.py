class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        n = len(bloomDay)
        low = min(bloomDay)
        high = max(bloomDay)
        if m*k > n:
            return -1
        while low <= high:
            mid = (low+high)//2
           
            if self.possible(bloomDay,mid,m,k):
                high = mid - 1
            else:
                low = mid + 1
        return low



    def possible(self,bloomDay,day,m,k):
        n = len(bloomDay)
        count = 0
        No_of_Bouque = 0
        for i in range(n):
            if bloomDay[i] <= day:
                count += 1
            else:
                No_of_Bouque += count//k
                count = 0
        No_of_Bouque += count//k
        if No_of_Bouque >= m:
            return True
        else:
            return False


        