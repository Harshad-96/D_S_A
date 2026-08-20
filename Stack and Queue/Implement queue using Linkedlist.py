class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0

    def push(self, x):
        temp = Node(x)
        if self.size == 0:
            self.start = temp
            self.end = temp
            self.size += 1
        else:
            self.end.next = temp
            self.end = temp
            self.size += 1
 

    def pop(self):
        if self.isEmpty():
            raise IndexError("Emety Queue")
        val = self.start.data
        self.start = self.start.next
        self.size -= 1
        if self.size == 0:
            self.end = None
        return val

    def peek(self):
        if self.isEmpty():
            raise IndexError("Queue Enety")
        return self.start.data
     

    def isEmpty(self):
        return self.size == 0
