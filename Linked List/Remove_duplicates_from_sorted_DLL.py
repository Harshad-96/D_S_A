# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def removeDuplicates(self, head):
        if head is None or head.next is None:
            return head
        temp = head
        while temp is not None:
            next_node = temp.next
            while next_node is not None and next_node.val == temp.val:
                doublecate = next_node
                next_node = next_node.next
            temp.next = next_node
            if next_node:
                next_node.prev = temp
            temp = temp.next
        return head