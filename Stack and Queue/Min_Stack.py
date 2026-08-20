class MinStack(object):

    def __init__(self):
        self.s = []
        self.min = 0
        

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        if not self.s:
            self.min = value
            self.s.append(value)
        else:
            if value < self.min:
                self.s.append(2*value - self.min)
                self.min = value
            else:
                self.s.append(value)

    def pop(self):
        """
        :rtype: None
        """
        if not self.s:
            raise IndexError("Emepty Stack")
        x = self.s[-1]
        self.s.pop()
        if x < self.min:
            self.min = 2*self.min - x
            
        

    def top(self):
        """
        :rtype: int
        """
        if not self.s:
            raise IndexError("Emety Stack")
        x = self.s[-1]
        if x < self.min:
            return self.min
        return x

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()