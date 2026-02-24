class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    nodes = []
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
        nodes.append(curr) 
    return dummy.next, nodes 


def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

# TEST
head, nodes = build_linked_list([1,1,2])
assert linked_list_to_list(Solution().deleteDuplicates(head)) == [1,2]
head, nodes = build_linked_list([1,1,2,3,3])
assert linked_list_to_list(Solution().deleteDuplicates(head)) == [1,2,3]
print("83 passed ✅")