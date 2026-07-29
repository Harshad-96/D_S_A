# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        temp = head
        prev_node = None

        while temp is not None:
            start = temp                     # remember this group's original start
            kthnode = funckth(temp, k)
            if kthnode is None:
                # fewer than k nodes left — leave them as-is
                if prev_node:
                    prev_node.next = temp
                break

            next_node = kthnode.next
            kthnode.next = None              # cut this group off from the rest
            new_start = reverse(temp)        # reverse this group, get its new head

            if start == head:
                head = new_start
            else:
                prev_node.next = new_start

            prev_node = start                # after reversal, 'start' is now the tail of this group
            temp = next_node

        return head


def funckth(temp, k):
    while k > 1:
        if temp is None:
            return None
        temp = temp.next
        k -= 1
    return temp if temp is not None else None


def reverse(temp):
    prev = None
    curr = temp
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev