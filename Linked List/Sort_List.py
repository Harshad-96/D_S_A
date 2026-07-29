# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        
        prev = None
        slow = head 
        fast = head
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        left_head = head
        right_head =  slow
        left = self.sortList(left_head)
        right = self.sortList(right_head)

        return mergeSort(left,right)

def mergeSort(left,right):
    dummy = ListNode(-1)
    temp = dummy
    t1 = left
    t2 = right
    while t1 is not None and t2 is not None:
        if t1.val < t2.val:
            temp.next = t1
            temp = t1
            t1 = t1.next
        else:
            temp.next = t2
            temp = t2
            t2 = t2.next
    if t1 is not None:
        temp.next = t1
        t1 = t1.next
    if t2 is not None:
        temp.next = t2
        t2 = t2.next
    return dummy.next