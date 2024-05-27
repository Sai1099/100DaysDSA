class Node:
    def __init__(self,data,next):
        self.data =data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head= None
    def insert_at_begin(self,data):
        node = Node(data,self.head)
        self.head = node
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
    def remove_at(self,index):
        if index<0 or  index>self.get_length():
            raise Exception('Invalid Index')
        if index == 0:
            self.head = self.head.next
            return
        itr  = self.head
        count = 0 
        while itr:
            if count == index - 1:
              itr.next = itr.next.next
              break
            itr = itr.next
            count +=1
    def add_at_index(self,x,index):
        if index == 0:
            return self.insert_at_begin(x)
        itr = self.head
        count = 0
        while itr:
            if count == index -1:
                new_node = Node(x,itr.next)
                itr.next = new_node
            itr = itr.next
            count+=1
    def search_for_index(self):
        itr = self.head
        dsg=[]
        while itr:
            dsg.append(str(itr.data))
            itr = itr.next
        return dsg
    def searching(self,val):
        itr = self.head
        while itr:
            if val == itr.data:
                print('tRUE')
                return
            itr = itr.next
        print('false')
       

    

    ##if we want to remove the specific node from it in List Node
    def remove_num(self,node):
        node.data = node.next.data
        node.next = node.next.next
    def print_ll(self):
        if self.head is None:
            return "Emoty"
        itr = self.head
        llist=' '
        while itr:
            llist += str(itr.data) + ' '
            itr = itr.next
        print(llist)
    


l1 = LinkedList()

l1.insert_at_begin(23)
l1.insert_at_begin(54)
l1.insert_at_end(5)
l1.insert_at_end(7)
l1.get_length()
l1.remove_at(2)
l1.add_at_index(99,0)
l1.search_for_index()
l1.searching(6)
l1.print_ll()
