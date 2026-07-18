class Solution:
    def maxLen(self, arr):
        # Your code goes here
        max_len = 0
        prefix_sum = 0
        n = len(arr)
        hashmap ={}
        for i in range(n):
            prefix_sum += arr[i]

            if prefix_sum == 0:
                max_len = i + 1
            if prefix_sum in hashmap:
                max_len = max(max_len,i - hashmap[prefix_sum]) 
            else:
                hashmap[prefix_sum] = i
        return max_len