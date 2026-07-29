# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return None
        count = 0
        temp = head
        while temp is not None:
            count += 1
            temp = temp.next
        # if count == 2:
        #     head.next = None
        #     return head
        n = count // 2
        temp = head
        while n > 1:
            temp = temp.next
            n -= 1
        temp.next = temp.next.next
        return head
