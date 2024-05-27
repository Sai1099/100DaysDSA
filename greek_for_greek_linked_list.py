arr=list(input())
class Node:
        def __init__(self,data,next):
            self.data =data
            self.next =next
        
class linkedlist():
        def __init__(self):
            self.head=None
        def insert_at_begin(self,data):
            
             node = Node(data,self.head)
             self.head = node
        def inset_at_end(self,data):
            if self.head is None:
                self.head = Node(data,None)
                return
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data,None)
        def print_ll(self):
            if self.head is None:
                print("Empty")
            itr = self.head
            llist=''
            while itr:
                llist+=str(itr.data) + ' '
                itr = itr.next
            print(llist)
l1 = linkedlist()
for i in range(len(arr)):
        l1.inset_at_end(arr[i])
l1.print_ll()
