"""
Problem: Middle of the Linked List
LeetCode: https://leetcode.com/problems/middle-of-the-linked-list/
Difficulty: Easy

Approach:
Use two pointers (slow & fast).
- Slow moves 1 step
- Fast moves 2 steps
When fast reaches the end, slow is at the middle.

Why this works:
Fast pointer travels twice as fast, so slow reaches the midpoint.

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
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        slow = fast = head
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
# TEST
head, nodes = build_linked_list([1,2,3,4,5])
assert Solution().middleNode(head).val == 3
head, nodes = build_linked_list([1,2,3,4,5,6])
assert Solution().middleNode(head).val == 4
print("876 passed ✅")
