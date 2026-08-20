class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        summ = 0
        r = n-1
        for i in range(k):
            summ += cardPoints[i]
        maxx = summ
        for i in range(k-1,-1,-1):
            summ -= cardPoints[i]
            summ += cardPoints[r]
            r -= 1
            maxx = max(maxx,summ)
        return maxx