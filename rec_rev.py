class Node:
    def __init__(self,newdata):
        self.data = newdata
        self.next = None
#Creating a recursive reverse function
def reverse_rec(head):
    if head is None or head.next is None:
        return head
    rest = reverse_rec(head.next)
    head.next.next = head
    head.next = None
    return rest
def printlist(head):
    while head:
        print(head.data,end='->')
        head = head.next
    print(None)
def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    printlist(head)
    rev_head = reverse_rec(head)
    printlist(rev_head)
if __name__ =='__main__':
    main()