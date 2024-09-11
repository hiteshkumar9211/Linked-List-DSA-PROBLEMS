class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

def pairwise_Swap(head):
   temp = head
   while temp is not None:
       if(temp.data != temp.next.data):
           temp.data,temp.next.data = temp.next.data,temp.data
       temp = temp.next.next

def printList(head):
    temp = head
    while temp is not None:
        print(temp.data,end='->')
        temp = temp.next
    print('None')
def main():
    node = Node(1)
    node.next = Node(2)
    node.next.next = Node(3)
    node.next.next.next = Node(2)
    print('Before pairwise swapping:')
    printList(node)
    pairwise_Swap(node)
    print('After pairwise swapping:')
    printList(node)
if __name__ == '__main__':
    main()

