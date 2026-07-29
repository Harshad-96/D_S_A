# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        temp = head 
        count = 1
        while temp.next is not None:
            count += 1
            temp = temp.next
        temp.next = head
        k = k % count
        k = count - k
        temp = head
        while k > 1:
            temp = temp.next
            k -= 1
        head = temp.next
        temp.next = None
        return head
        