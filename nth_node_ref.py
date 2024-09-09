class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

def nthLast(head,N):
    length = 0
    ref_node = head
    main_node = head
    for i in range(1,N):
        ref_node = ref_node.next
    if ref_node is None:
        return -1
    while ref_node.next is not None:
        ref_node = ref_node.next
        main_node = main_node.next
    return main_node.data
def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    ans = nthLast(head,2)
    return ans
if __name__ == '__main__':
    print(main());

    