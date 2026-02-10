class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        curr = dummy 

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        curr.next = list1 or list2
        return dummy.next
    

# TEST
l1 = build_linked_list([1,2,4])
l2 = build_linked_list([1,3,4])
assert linked_list_to_list(Solution().mergeTwoLists(l1, l2)) == [1,1,2,3,4,4]
print("21 passed ✅")