class Solution:   
    def singleNumber(self, nums):
        #your code goes here
        xor = 0
        for num in nums:
            xor ^= num
        rightmost = (xor & xor-1)^xor
        b1 = 0
        b2 = 0
        for num in nums:
            if num & rightmost:
                b1 ^= num
            else:
                b2 ^= num
        return [b1,b2]