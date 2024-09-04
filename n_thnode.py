class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#Creating a function for getting nth node from last
def nthNode(head,N):
    temp = head
    length = 0
    while temp:
        temp = temp.next
        length += 1
    if N > length:
        return 'dont make a fool of me!!'
    temp = head
    for i in range(1,length - N):
        temp = temp.next
    return temp.data
def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    ans = nthNode(head,0)
    return ans
if __name__ == '__main__':
    print(main());