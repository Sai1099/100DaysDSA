t = int(input())
class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next
class linked_list:
    def __init__(self):
        self.head = None
    def insert_at_begin(self,data):
        
        node =Node(data,self.head)
        self.head = node
    def print_ll(self):
        if self.head is None:
            print("The Linked_List Is Empty")
        
        itr = self.head
        llist = ''
        while itr:
            llist+=str(itr.data) + ' '
            itr = itr.next
        
        print(llist)


l1 = linked_list()
for i in range(1,t+1):
    l1.insert_at_begin(i)
#l1.insert_at_begin(5)
#l1.insert_at_begin(3523)
l1.print_ll()