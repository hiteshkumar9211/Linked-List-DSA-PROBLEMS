class Node:
    def __init__(self,x):
        self.data = x
        self.next = None
#Creating a function for deleting the middle element
def deleteMiddle(head):
   if head is None:
       return None
   prev = None
   fast = head
   slow = head
   while fast and fast.next:
       fast = fast.next.next
       prev = slow 
       slow = slow.next
   prev.next = slow.next
   return head


def printList(head):
    while head is not None:
       print(head.data,end='->')
       head = head.next
    print(None)

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Original Linked List:", end=" ")
printList(head)

# Delete the middle node.
head = deleteMiddle(head)

print("Linked List after deleting the middle node:", end=" ")
printList(head)
