class Solution:
    def fractionalKnapsack(self, val, wt, cap):
        # Your code goes here
        items = [(val[i]/wt[i],val[i],wt[i]) for i in range(len(val))]

        items.sort(key = lambda x : x[0], reverse = True)

        total_val = 0
        remaining = cap

        for ratio,v,w in items:
            if remaining == 0:
                break
            if w <= remaining:
                total_val += v
                remaining -= w
            else:
                total_val += ratio*remaining
                remaining = 0
        return round(total_val,6)