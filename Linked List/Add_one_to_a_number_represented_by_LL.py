# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addOne(self, head):
        carry = helper(head)
        if carry == 1:
            new_node = ListNode(1)
            new_node.next = head
            head = new_node
        return head

def helper(temp):
    if temp == None:
        return 1
    carry = helper(temp.next)
    temp.val += carry
    if temp.val < 10:
        return 0
    else:
        temp.val = 0
        return 1