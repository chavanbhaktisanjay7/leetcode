"""
Basic Stack Implementation in Python
Operations:
- push
- pop
- peek
- is_empty
- size

Stack follows LIFO principle (Last In First Out).
"""


class Stack:
    def __init__(self):
        self.items = []

    # Push element onto stack
    def push(self, value):
        self.items.append(value)

    # Pop element from stack
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    # Peek top element
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    # Check if stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Get stack size
    def size(self):
        return len(self.items)

    # Print stack (top at right)
    def display(self):
        print("Stack:", self.items)

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {')':'(','}':'{',']':'['}
        for ch in s:
            if ch in pairs.values():
                stack.append(ch)
            else:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()

        return len(stack)==0
        
            
# TEST
assert Solution().isValid("()") == True
assert Solution().isValid("()[]{}") == True
assert Solution().isValid("(]") == False
assert Solution().isValid("([)]") == False
assert Solution().isValid("{[]}") == True
print("20 passed ✅")

