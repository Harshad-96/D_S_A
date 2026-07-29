class Solution:
    def insertAtHead(self, head, X):
        """
        :type head: Optional[ListNode]
        :type X: int
        :rtype: Optional[ListNode]
        """
        temp = ListNode(X)
        temp.next = head
        head = temp
        return head


def convert_arr_to_ll(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


if __name__ == "__main__":
    arr = [1, 2, 3]
    X = 7

    head = convert_arr_to_ll(arr)
    sol = Solution()
    head = sol.insertAtHead(head, X)
    print_list(head)