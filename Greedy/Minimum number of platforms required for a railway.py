class Solution:
    def findPlatform(self, Arrival, Departure):
        #your code goes here
        Arrival.sort()
        Departure.sort()
        maxplatforms = 0
        count = 0
        l = 0
        r = 0
        while l < len(Arrival) and r < len(Departure):
            if Arrival[l] <= Departure[r]:
                count += 1
                l += 1
            else:
                count -= 1
                r += 1
            maxplatforms = max(maxplatforms,count)
        return maxplatforms