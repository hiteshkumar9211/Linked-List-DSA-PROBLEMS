class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def detect_loop(head):
    node_set = set()
    while head:
        if head in node_set:
            return True
        node_set.add(head)
        head = head.next
    return False
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head.next.next.next.next.next = Node(60)

# Creating a loop resulting in the linked list:
# 10 -> 20 -> 30 -> 40 -> 10 -> 20 -> 30 ...
head.next.next.next.next = head
print(detect_loop(head))
