class ArrayStack:
    def __init__(self):
        self.items = []

    def push(self, x):
        return self.items.append(x)

    def pop(self):
        if not self.items:
            raise IndexError("pop from emety stack")
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0
