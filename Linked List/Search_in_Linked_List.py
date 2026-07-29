"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
"""
        
class Solution:
    def searchKey(self, head, key):
        # Your code goes here
        if head is None:
            return head
        current = head 
        while current is not None:
            if current.val == key:
                return True
            else:
                current = current.next
        return False