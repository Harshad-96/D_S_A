# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def deleteAllOccurrences(self, head, target):
        temp = head
        if head is None:
            return None
        while temp is not None:  
            if temp.val == target:
                if temp == head:
                    head = temp.next
                next_node = temp.next
                prev_node = temp.prev
                if next_node is not None:
                    next_node.prev = prev_node
                if prev_node is not None:
                    prev_node.next = next_node
                temp.next = None
                temp.prev = None
                temp = next_node
            else:
                temp = temp.next
        return head