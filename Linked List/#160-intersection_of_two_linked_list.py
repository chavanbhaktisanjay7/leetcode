"""
Problem: Intersection of Two Linked Lists
LeetCode: https://leetcode.com/problems/intersection-of-two-linked-lists/
Difficulty: Easy

Approach:
Use two pointers traversing both lists.
When one pointer reaches the end,
switch it to the other list.

They will meet at:
- intersection node, or
- None

Time Complexity: O(n + m)
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
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a = headA
        b = headB
        while a!=b:
            a = a.next if a else headB
            b = b.next if b else headA
            
        return a    
 # shared part
common_head, common_nodes = build_linked_list([8,4,5])

# list A
headA, nodesA = build_linked_list([4,1])
nodesA[-1].next = common_head

# list B
headB, nodesB = build_linked_list([5,6,1])
nodesB[-1].next = common_head

assert Solution().getIntersectionNode(headA, headB).val == 8
print("160 passed ✅")