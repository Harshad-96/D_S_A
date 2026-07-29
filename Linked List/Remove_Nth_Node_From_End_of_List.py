# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return None
        count = 0
        temp = head
        while temp is not None:
            count += 1
            temp = temp.next
        n = count - n
        if n ==0:
            return head.next
        temp = head
        while n > 1:
            temp = temp.next
            n -= 1
        temp.next = temp.next.next
        return head


        