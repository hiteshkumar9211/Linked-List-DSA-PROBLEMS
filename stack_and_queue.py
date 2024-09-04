# Problem 1: Stack Implementation
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return None

    def top(self):
        if not self.isEmpty():
            return self.stack[-1]
        return None

    def isEmpty(self):
        return len(self.stack) == 0

# Problem 2: Valid Parentheses
def isValidParentheses(s):
    stack = Stack()
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            if stack.isEmpty() or stack.top() != mapping[char]:
                return False
            stack.pop()
        else:
            stack.push(char)
    return stack.isEmpty()

# Problem 3: Stack with Minimum
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if not self.stack:
            return None
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()
        return

    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]

# Problem 4: Valid Palindrome
def isPalindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Problem 5: Backspace String Compare
def backspaceCompare(s, t):
    def processString(s):
        stack = []
        for char in s:
            if char != '#':
                stack.append(char)
            elif stack:
                stack.pop()
        return ''.join(stack)

    return processString(s) == processString(t)

# Problem 6: Queue Implementation
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        return None

    def front(self):
        if not self.isEmpty():
            return self.queue[0]
        return None

    def rear(self):
        if not self.isEmpty():
            return self.queue[-1]
        return None

    def isEmpty(self):
        return len(self.queue) == 0

# Problem 7: Stack Implementation Using Queues
class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        self.q2.enqueue(x)
        while not self.q1.isEmpty():
            self.q2.enqueue(self.q1.dequeue())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if not self.q1.isEmpty():
            return self.q1.dequeue()
        return None

    def top(self):
        if not self.q1.isEmpty():
            return self.q1.front()
        return None

    def isEmpty(self):
        return self.q1.isEmpty()

# Problem 8: Palindrome Linked List
class Node:
    def __init__(self, data):

        self.data = data
        self.ptr = None
def ispalindrome(head):

    # Temp pointer
    slow = head

    # Declare a stack
    stack = []

    ispalin = True

    # Push all elements of the list
    # to the stack
    while slow != None:
        stack.append(slow.data)

        # Move ahead
        slow = slow.ptr

    # Iterate in the list again and
    # check by popping from the stack
    while head != None:

        # Get the top most element
        i = stack.pop()

        # Check if data is not
        # same as popped element
        if head.data == i:
            ispalin = True
        else:
            ispalin = False
            break

        # Move ahead
        head = head.ptr

    return ispalin

# Problem 1: Stack Implementation
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.top())  # Output: 3
print(stack.pop())  # Output: 3
print(stack.top())  # Output: 2
# Problem 2: Valid Parentheses
print(isValidParentheses("()"))  # Output: True
print(isValidParentheses("()[]{}"))  # Output: True
print(isValidParentheses("(]"))  # Output: False

# Problem 3: Stack with Minimum
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.getMin())  # Output: -3
min_stack.pop()
print(min_stack.getMin())
# Output: -2

# Problem 4: Valid Palindrome
print(isPalindrome("A man, a plan, a canal, Panama!"))  # Output: True
print(isPalindrome("racecar"))  # Output: True
print(isPalindrome("abcdcba"))  # Output: False

# Problem 5: Backspace String Compare
print(backspaceCompare("ab#c", "ad#c"))  # Output: True
print(backspaceCompare("ab##", "c#d#"))  # Output: True
print(backspaceCompare("a#c#", "b#"))  # Output: False

# Problem 6: Queue Implementation
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.front())  # Output: 1
print(queue.dequeue())  # Output: 1
print(queue.front())  # Output: 2

# Problem 7: Stack Implementation Using Queues
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.top())  # Output: 3
print(stack.pop())  # Output: 3
print(stack.top())  # Output: 2

# Problem 8: Palindrome Linked List
head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(1)
print(ispalindrome(head))  # Output: True
    