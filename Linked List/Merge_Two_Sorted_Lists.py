# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy_node = ListNode(-1)
        temp = dummy_node
        t1 = list1
        t2 = list2
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
        return dummy_node.next