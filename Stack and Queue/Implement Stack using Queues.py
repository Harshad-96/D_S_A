from collections import deque
class MyStack(object):

    def __init__(self):
        self.stack = deque()
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        for _ in range(len(self.stack)-1):
            self.stack.append(self.stack.popleft())
        
    def pop(self):
        """
        :rtype: int
        """
        if not self.stack:
            raise IndexError("Delet from Emety satck")
        return self.stack.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()