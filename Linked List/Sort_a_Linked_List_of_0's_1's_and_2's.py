# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next

class Solution:
    def sortList(self, head):
        if head is None or head.next is None:
            return head
        zero_head = ListNode(-1)
        one_head = ListNode(-1)
        two_head = ListNode(-1)
        zero = zero_head
        one = one_head
        two = two_head
        temp = head
        while temp is not None:
            if temp.data == 0:
                zero.next = temp
                zero = temp
                temp = temp.next
            elif temp.data == 1:
                one.next = temp
                one = temp
                temp = temp.next
            else:
                two.next = temp
                two = temp
                temp = temp.next
        zero.next = one_head.next if one_head.next else two_head.next
        one.next = two_head.next
        two.next = None
        return zero_head.next

