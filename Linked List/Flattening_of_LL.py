# Definiton of singly Linked List
# class ListNode:
#     def __init__(self, val=0, next=None, child=None):
#         self.val = val
#         self.next = next
#         self.child = child

class Solution:
    def flattenLinkedList(self, head):
        if head is None or head.next is None:
            return head
        mergehead = self.flattenLinkedList(head.next)
        head =  merge(head,mergehead)
        return head


def merge(list1,list2):
    dummy = ListNode(-1)
    res = dummy
    while list1 is not None and list2 is not None:
        if list1.val < list2.val:
            res.child = list1
            res = list1
            list1 = list1.child
        else:
            res.child = list2
            res = list2
            list2 = list2.child
        res.next = None
    if list1:
        res.child = list1
        res = list1
        res.next = None
        list1 = list1.child
    if list2:
        res.child = list2
        res = list2
        res.next = None
        list2 = list2.child
    return dummy.child