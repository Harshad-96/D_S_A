class Solution:
    def kDistinctChar(self, s, k):
        #your code goes here
        summ = 0
        maxx = 0
        l = 0
        dic = {}
        for i in range(len(s)):
            dic[s[i]] = dic.get(s[i],0) + 1

            if len(dic) > k:
                dic[s[l]] -= 1
                if dic[s[l]] == 0:
                    del dic[s[l]]
                l += 1
            maxx = max(maxx,i-l+1)
        return maxx