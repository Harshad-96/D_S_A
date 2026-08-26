class Solution:
    def JobScheduling(self, Jobs):
        #your code goes here
        Jobs.sort(key=lambda x:x[2],reverse = True)

        maxIndex = -1
        maxIndex = max(i[1] for i in Jobs)

        slots = [False] * (maxIndex + 1)
        count = 0
        maxProfit = 0

        for jobId, deadline, profit in Jobs:
            for t in range(min(deadline,maxIndex),0,-1):
                if not slots[t]:
                    count += 1
                    slots[t] = True
                    maxProfit += profit
                    break
        return count, maxProfit

