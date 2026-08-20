# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        import heapq
        ans = []
        for i,node in enumerate(lists):
            if node:
                heapq.heappush(ans,(node.val,i,node))

        dummy = ListNode(-1)
        temp = dummy

        while ans:
            val,ind,node = heapq.heappop(ans)
            if node.next:
                heapq.heappush(ans,(node.next.val,ind,node.next))
            temp.next = node
            temp = temp.next
        return dummy.next