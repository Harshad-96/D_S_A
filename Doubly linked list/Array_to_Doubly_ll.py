class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None
    
def Array_to_2ll(arr):
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        new_node = Node(val)
        new_node.prev = current
        current.next = new_node
        current = current.next
    return head
    
def print_2ll(head):
    current = head 
    while current is not None:
        print(current.val,end = " -> ")
        current = current.next
    print("None")

arr = [1,2,3,4,5]
head = Array_to_2ll(arr)
print_2ll(head)
