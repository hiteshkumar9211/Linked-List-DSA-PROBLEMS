class Node:
    def __init__(self,x):
        self.data = x 
        self.next = None

def detectLoop(head):
    fast_ptr = head
    slow_ptr = head
    while (slow_ptr,fast_ptr,fast_ptr.next):
        if (fast_ptr == slow_ptr):
            return True
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next
    return False


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head.next.next.next.next.next = head
print(detectLoop(head))
