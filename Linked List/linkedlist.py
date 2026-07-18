class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def convert_arr_to_ll(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head


def remove_tail(head):
    if head is None or head.next is None:
        return None
    temp = head
    while temp.next.next is not None:
        temp = temp.next
    temp.next = None
    return head


def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

def removeKth(head,k):
    if head is None :
        return head
    if k == 1:
        return head.next
    count = 0
    temp = head
    prev = None
    while temp is not None:
        count += 1
        if count == k:
            prev.next = prev.next.next
            break
        prev = temp
        temp = temp.next
    return head
        




if __name__ == "__main__":
    arr = [12, 5, 8, 7]
    head = convert_arr_to_ll(arr)
    # head = remove_tail(head)
    
    head = removeKth(head,2)
    print_list(head)