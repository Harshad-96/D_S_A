class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        n = len(fruits)
        l = 0
        r = 0
        dic = {}
        maxlen = 0
        while r < n:
            dic[fruits[r]] = dic.get(fruits[r],0) + 1
            if len(dic) > 2:
                dic[fruits[l]] -= 1
                if dic[fruits[l]] == 0:
                    del dic[fruits[l]]
                l += 1
            if len(dic) <= 2:
                    maxlen = max(maxlen,r-l+1)
            r += 1
        return maxlen