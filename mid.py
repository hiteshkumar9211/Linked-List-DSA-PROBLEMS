#Middle of a linked list using fast and slow pointers
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def get_Middle(head):
    slow_ptr = head
    fast_ptr = head
    while fast_ptr is not None and fast_ptr.next is not None:
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next
    return slow_ptr.data
def main():
    head = Node(4)
    head.next = Node(12)
    head.next.next = Node(39)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(45)
    return get_Middle(head)
if __name__ == '__main__':
  print(main())