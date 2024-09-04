#Defination of node using class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#Linked list using class
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    #Prepend at the first position.
    def prepend(self, newdata):
       newnode = Node(newdata)
       newnode.next = self.head
       self.head = newnode
       self.length += 1
    #append at the last position.
    def append(self, newdata):
        newnode = Node(newdata)
        if self.head is None:
            self.head = newnode
            self.length = 1
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode
        self.length += 1
    #inserting linked list position wise.
    def insert(self, position, data):
        if position > self.length:
           self.append(data)
        elif position == 0:
           self.prepend(data)
        else:
            newnode = Node(data)
            current_node = self.head
            for i in range(position - 1):
                current_node = current_node.next
            newnode.next = current_node.next
            current_node.next = newnode
            self.length += 1
    #deleting element in first position of linked list.
    def delete_at_begin(self):
        if self.head is None:
            return
        current = self.head
        self.head = self.head.next
        del current
        self.length -= 1
    #deleting element in last position of linked list
    def delete_at_end(self):
       second_last = self.head
       if self.head is None:
           return
       if self.head.next is None:
           return
       while second_last.next.next:
           second_last = second_last.next
       second_last.next = None
       self.length -= 1

    def delete_at_position(self,position):
       if self.head is None:
           return 
       if position == 1:
           self.delete_at_begin()
       elif position > self.length:
           self.delete_at_end()
       else:
           current = self.head
           for i in range(position - 1):
               current = current.next
           current = current.next
           self.length -= 1

    #removing duplicates in a list
    def remove_duplicates(self):
       seen = set()
       current = self.head
       prev = None
       while current:
           if current.data in seen:
               prev.next = current.next
               del current
               current = prev.next
               self.length -= 1
           else:
               seen.add(current.data)
               prev = current
               current = current.next
    #function for merginf of two linked lists.
    def merge(self,other):
      if self.head is None:
          self.head = other.node
          return
      if other.head is None:
          return
      temp1 = self.head
      temp2 = other.head
      prev = None
      while temp1 and temp2:
          if temp1.data <= temp2.data:
              if prev is None:
                  self.head = temp1
              prev = temp1
              temp1 = temp1.next
          else:
              if prev:
                  prev.next = temp2
              else:
                  other.head = temp2
              prev = temp2
              temp2 = temp2.next
      if temp1:
          prev.next = temp1
      if temp2:
          prev.next = temp2
    def rotate(self, k):
        if k==0:
            return

        node=self.head
        cnt=1
        while cnt<k and node is not None:
            node=node.next
            cnt+=10 


        if node is None:
            return

        keyNode=node

        while node.next is not None:
            node=node.next

        node.next=self.head
        self.head=keyNode.next
        keyNode.next=None
    #printing linked list.
    def printList(self):
        temp = self.head
        while temp:
            print(str(temp.data),end='->')
            temp = temp.next
        print(None)
    #printing length of linked list.
    def printLength(self):
        print('Length of list is:', self.length)
    #reversal function for linked list.
    def print_reversal(self):
      stack = []
      temp = self.head
      while temp:
          stack += [temp.data]
          temp = temp.next
      for i in range(len(stack)):
          print(stack[-(i + 1)],end='->')
      print(None)
 

# Driver Code
llist = LinkedList()
llist.append(1)
llist.prepend(0)
llist.insert(2,2)
llist.append(3)
llist.append(4)
llist.printList()
llist.printLength()
llist.print_reversal()
llist.delete_at_begin()
llist.printList()
llist.printLength()
llist.delete_at_end()
llist.printList()
llist.printLength()
llist.print_reversal()
llist.remove_duplicates()
llist.printList()
llist.printLength()
llist.insert(2,3)
llist.insert(2,3)
llist.printList()
llist.printLength()
llist.remove_duplicates()
llist.printList()
llist1 = LinkedList()
llist1.append(4)
llist1.append(5)
llist1.append(6)
# llist1.printList()
# llist.merge(llist1)
# llist.printList()
llist1.append(8)
llist1.append(9)
llist1.printList()
llist1.rotate(2)
llist1.printList()
