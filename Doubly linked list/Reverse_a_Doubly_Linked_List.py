# class ListNode:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None

class Solution:
    def reverseDLL(self, head):
        # Your code goes here
        if head.prev is None and head.next is None:
            return head
        current = head
        
        while current is not None:
            last = current.prev
            current.prev = current.next
            current.next = last
            current = current.prev
        return last.prev