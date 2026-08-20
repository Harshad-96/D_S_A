class Solution:
    def count_NGE(self, arr, indices):
        # Your code goes here
        count = 0
        ans = []
        n = len(arr)
        for num in indices:
            for i in range(num+1,n):
                if arr[num] < arr[i]:
                    count += 1
            ans.append(count)
            count = 0
        return ans