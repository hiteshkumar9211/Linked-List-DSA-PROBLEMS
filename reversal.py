class Node:
    def __init__(self,x):
        self.data = x
        self.next = None
#creating function for reversal of linked list.
def reversal(head):
    curr = head
    prev = None
    while curr is not None:
        nextnode = curr.next
        curr.next = prev
        prev = curr 
        curr = nextnode
    return prev
#creating a function for printing of linked list.
def print_list(head):
    while head is not None:
        print(head.data,end='->')
        head = head.next
    print(None)
def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    print_list(head)
    rev = reversal(head)
    print_list(rev)
if __name__ == '__main__':
    main()