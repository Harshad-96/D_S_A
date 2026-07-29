class Solution:      
    def findRangeXOR(self, l, r):
        #your code goes here
        return self.fint1ToN(l-1) ^ self.fint1ToN(r)
    
    def fint1ToN(self,n):
        if n%4 == 1:
            return 1
        elif n%4 == 2:
            return n+1
        elif n%4 == 3:
            return 0
        else:
            return n