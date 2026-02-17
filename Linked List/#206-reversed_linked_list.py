"""
Problem: Reverse Linked List
LeetCode: https://leetcode.com/problems/reverse-linked-list/
Difficulty: Easy

Approach:
Iterative pointer reversal.
- Maintain previous, current, and next pointers
- Reverse links one by one

Key Insight:
Reversing a linked list is about changing directions, not values.

Time Complexity: O(n)
Space Complexity: O(1)
"""
def build_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    nodes = []

    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
        nodes.append(curr)

    return dummy.next, nodes

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        prev = None
        curr = head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        
# TEST
head, nodes = build_linked_list([1,2,3,4,5])    
assert Solution().reverseList(head).val == 5
print("206 passed ✅")
