
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        rev = self.reverseList(head.next)  # Recursively reverse the rest of the linked list

        head.next.next = head
        head.next = None

        return rev

# Helper function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test the reverseList function
if __name__ == "__main__":
    solution = Solution()
    head = create_linked_list([1, 2, 3, 4, 5])
    print("Original linked list:")
    print(linked_list_to_list(head))

    reversed_head = solution.reverseList(head)
    print("Reversed linked list:")
    print(linked_list_to_list(reversed_head))
