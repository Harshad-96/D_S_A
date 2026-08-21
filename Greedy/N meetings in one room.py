class Solution:
    def maxMeetings(self, start, end):
        #your code goes here
        meatings = [(start[i],end[i]) for i in range(len(start))]

        meatings.sort(key = lambda x:x[1])

        count = 0
        last_meating = -1
        for s,e in meatings:
            if last_meating < s:
                count += 1
                last_meating = e 
        return count  
        