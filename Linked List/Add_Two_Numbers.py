# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        temp = dummy
        carry = 0
        while l1 is not None or l2 is not None or carry:
            summ = 0
            if l1 is not None:
                summ += l1.val
                l1 = l1.next
            if l2 is not None:
                summ += l2.val
                l2 = l2.next
            
            summ += carry
            carry = summ//10
            node = ListNode(summ%10)
            temp.next = node
            temp = node
        return dummy.next
        