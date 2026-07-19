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

def Delete_head(head):
    if head is None:
        return head
    head = head.next
    if head is not None:
        head.prev = None
    return head
        
def Delete_tail(head):
    if head is None:
        return head
    if head.next is None:
        return None
    current = head
    while current.next is not None:
        current = current.next
    prev = current.prev
    current.prev = None
    prev.next = None
    return head


def delete_kth_element(head,k):
    current = head
    count = 0
    while current is not None:
        count += 1

        if k == count:
            break
        current = current.next
    if current is None:
        print("kth is out of range")
        return head
    back = current.prev
    front = current.next
    if back is None and front is None:
        return None
    elif back is None:
        return Delete_head(head)
    elif front is None:
        return Delete_tail(head)
    else:
        back.next = front
        front.prev = back
        current.prev = None
        current.next = None
    return head


arr = [1,2,3,4,5]
head = Array_to_2ll(arr)
# print_2ll(head)
# head = Delete_head(head)
# print_2ll(head)
# head = Delete_tail(head)
# print_2ll(head)
head = delete_kth_element(head,6)
print_2ll(head)