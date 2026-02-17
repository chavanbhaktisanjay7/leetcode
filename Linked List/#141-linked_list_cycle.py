"""
Problem: Linked List Cycle
LeetCode: https://leetcode.com/problems/linked-list-cycle/
Difficulty: Easy

Approach:
Use two pointers:
- Slow moves 1 step
- Fast moves 2 steps

If a cycle exists, they will eventually meet.
If fast reaches None, there is no cycle.

Time Complexity: O(n)
Space Complexity: O(1)
"""
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
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
                
        return False
    

# TEST 1: list with cycle
head, nodes = build_linked_list([3,2,0,-4])
nodes[-1].next = nodes[1]  # create cycle

assert Solution().hasCycle(head) == True


# TEST 2: list without cycle
head2, _ = build_linked_list([1,2,3,4])
assert Solution().hasCycle(head2) == False

print("141 passed ✅")