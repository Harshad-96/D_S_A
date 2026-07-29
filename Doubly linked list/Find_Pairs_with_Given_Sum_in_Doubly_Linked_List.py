'''
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
'''

class Solution:
    def findPairsWithGivenSum(self, head, target):
        # Your code goes here
        arr = []
        tail = head
        while tail.next is not None:
            tail = tail.next

        start = head
        while start.val < tail.val:
            if start.val + tail.val > target:
                tail = tail.prev
            elif start.val + tail.val < target:
                start = start.next
            else:
                arr.append([start.val,tail.val])
                start = start.next
                tail = tail.prev
        return arr