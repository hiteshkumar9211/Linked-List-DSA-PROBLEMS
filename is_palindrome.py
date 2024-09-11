class Node:
    def __init__(self,x):
        self.data = x
        self.next = None


def revList(head):
    prev = None
    curr = head
    while curr is not None:
        nextnode = curr.next 
        curr.next = prev
        prev = curr
        curr = nextnode
    return prev 
def isIdentical(head1,head2):
    while head1 and head2:
        if(head1.data != head2.data):
            return False
        head1 = head1.next
        head2 = head2.next
    return True
def printList(head):
    temp = head
    while temp is not None:
        print(temp.data,end='->')
        temp = temp.next
    print('None')
def isPalindrome(head):
    if head is None or head.next is None:
        return True
    slow,fast = head,head
    while fast.next and fast.next.next:
        slow = slow.next 
        fast = fast.next
def main():
    node1 = Node(0)
    node1.next = Node(0)
    node1.next.next = Node(0)
    node1.next.next.next = Node(0)
    node1.next.next.next.next = Node(0)
    result = isPalindrome(node1)
    if result :
        return True
    else:
        return False
    
if __name__ == '__main__':
    print(main())
