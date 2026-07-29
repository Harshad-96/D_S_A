class Solution:
    def getLength(self, head):
        # Your code goes here
        current = head 
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count
