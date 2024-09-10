# Python Program to sort a linked list of 0s, 1s or 2s

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

# Function to sort a linked list of 0s, 1s and 2s
def sort_list(head):
  
    # Initialize count of '0', '1' and '2' as 0
    cnt = [0, 0, 0]
    ptr = head
    while ptr is not None:
        cnt[ptr.data] += 1
        ptr = ptr.next

    idx = 0
    ptr = head

   
    while ptr is not None:
        if cnt[idx] == 0:
            idx += 1
        else:
            ptr.data = idx
            cnt[idx] -= 1
            ptr = ptr.next

def print_list(node):
    while node is not None:
        print(f" {node.data}", end='->')
        node = node.next
    print("None")


if __name__ == "__main__":

    # Create a hard-coded linked list:
    # 1 -> 1 -> 2 -> 1 -> 0 -> NULL
    head = Node(1)
    head.next = Node(1)
    head.next.next = Node(2)
    head.next.next.next = Node(1)
    head.next.next.next.next = Node(0)

    print("Linked List before Sorting:", end='')
    print_list(head)
    
    sort_list(head)

    print("Linked List after Sorting:", end='')
    print_list(head)
