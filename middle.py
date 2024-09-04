#Middle of a linked list using get length function.
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
#making a getlength function to print length of linked list
def getLength(head):
    length = 0
    while head:
        head = head.next
        length += 1
    return length

#getting the middle of linked list.
def midLength(head):
    mid_idx = getLength(head)//2
    while mid_idx:
        head = head.next
        mid_idx -= 1
    return head.data
#defining main function
def main():
    head = Node(4)
    head.next = Node(12)
    head.next.next = Node(39)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(45)
    return midLength(head)
if __name__ == "__main__":
    print(main())

