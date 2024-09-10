class Node:
    def __init__(self,x):
        self.data = x
        self.next = None
#Creating a function for deleting the middle element
def deleteMiddle(head):
    count = 0
    ptr_1 = head
    ptr_2 = head
    while ptr_1 is not None:
        ptr_1 = ptr_1.next
        count += 1
    mid = count//2
    for i in range(mid-1):
        ptr_2 = ptr_2.next
    ptr_2.next = ptr_2.next.next
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