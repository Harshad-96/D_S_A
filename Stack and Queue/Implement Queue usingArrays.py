from collections import deque
class ArrayQueue:
    def __init__(self):
        self.items = deque()
    def push(self, x):
        return self.items.append(x)

    def pop(self):
        if not self.items:
            raise IndexError("pop from emety list")
        return self.items.popleft()

    def peek(self):
        return self.items[0]

    def isEmpty(self):
        return len(self.items) == 0
