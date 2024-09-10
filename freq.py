class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

def countFreq(head,key):
    temp = head
    count = 0
    while temp is not None:
        if (temp.data == key):
            count += 1
        temp = temp.next
    return count
node = Node(1)
node.next = Node(1)
node.next.next = Node(2)
node.next.next.next = Node(3)
node.next.next.next.next = Node(4)
print(countFreq(node,1))