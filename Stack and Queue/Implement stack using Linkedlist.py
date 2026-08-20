class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, x):
        temp = Node(x)
        temp.next = self.head
        self.head = temp
        self.size += 1
        

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is Emety")
        val = self.head.data
        self.head = self.head.next
        self.size -= 1
        return val


    def top(self):
        if self.isEmpty():
            raise IndexError("Stack is Emety")
        return self.head.data
     

    def isEmpty(self):
        return self.size == 0
