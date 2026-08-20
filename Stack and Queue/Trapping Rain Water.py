class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        # prefix = [0]*n
        # prefix[0] = height[0]
        # for i in range(1,n):
        #     prefix[i] = max(height[i],prefix[i-1])
        # sufix = [0]*n
        # sufix[n-1] = height[n-1]
        # for i in range(n-2,-1,-1):
        #     sufix[i] = max(height[i],sufix[i+1])
        # total = 0
        # for i in range(n):
        #     left = prefix[i]
        #     right = sufix[i]
        #     if left > height[i] and right > height[i]:
        #         total += min(left,right) - height[i]
        # return total
        lmax = 0
        rmax = 0
        total = 0
        i = 0
        j = n-1
        while i < j:
            if height[i] <= height[j]:
                if lmax > height[i]:
                    total += lmax - height[i]
                else:
                    lmax = height[i]
                i += 1
            
            else:
                if rmax > height[j]:
                    total += rmax - height[j]
                else:
                    rmax = height[j]
                j -= 1
        return total