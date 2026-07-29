class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == divisor:
            return 1
        sign = 1
        if dividend < 0 and divisor >= 0:
            sign = -1
        if dividend >= 0 and divisor < 0:
            sign = -1
        ans = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            count = 0
            while dividend >= (divisor * (1 << (count+1))):
                count += 1
            ans += 1<<count
            dividend -= divisor << count
        if ans == 1<<31 and sign == 1:
            return 2**31 -1
        if ans == 1 << 31 and sign == -1:
            return -(2**31)
        return sign * ans
        