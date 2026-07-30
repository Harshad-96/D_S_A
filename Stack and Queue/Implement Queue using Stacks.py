class MyQueue(object):

    def __init__(self):
        self.st1 = []
        self.st2 = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.st1.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if not self.st2:
            if not self.st1:
                raise IndexError("Queue is Emety")
            while self.st1:
                self.st2.append(self.st1.pop())
        return self.st2.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if not self.st2:
            if not self.st1:
                raise IndexError("Queue is emety")
            while self.st1:
                self.st2.append(self.st1.pop())
        return self.st2[-1]        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.st1) == 0 and len(self.st2) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()