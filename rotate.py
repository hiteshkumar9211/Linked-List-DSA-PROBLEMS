class Node:
    def __init__(self,x):
        self.data = x
        self.next = None
def rotateList(head,key):
   if key == 0:
       return 
   count = 1
   node = head
   while count < key and node.next is not None:
       node = node.next
       count += 1
   keynode = node 
   while node.next is not None:
       node = node.next
   node.next = head
   head = keynode.next
   keynode.next = None
   return head
         
def printList(head):
    temp = head
    while temp:
        print(temp.data,end='->')
        temp = temp.next
    print(None)
def main():
    pos  = 2
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    printList(head)
    rot = rotateList(head,pos)
    printList(rot)
if __name__ == '__main__':
    main()