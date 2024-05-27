class Node:
    def __init__(self,data,next = None,prev =None):
      self.data =data
      self.next =next
      self.prev = prev
class Double_ll:
   def __init__(self):
      self.head = None
   def insert_at_begin(self,data):
      node = Node(data,self.head)
      if self.head is not None:
         self.head.prev = node
      self.head = node
   def insert_at_end(self,data):
      if self.head is None:
         self.head = Node(data)
      itr = self.head
      while itr.next:
         itr = itr.next
      new_node = Node(data)
      itr.next = new_node
      self.head.prev = new_node
   def delete_at_index(self, index):
        if self.head is None:
            return
        
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        
        itr = self.head
        count = 0
        while itr:
            if count == index:
                if itr.next:
                    itr.next.prev = itr.prev
                if itr.prev:
                    itr.prev.next = itr.next
                break
            itr = itr.next
            count += 1

   def print_ll_reverse(self):
        if self.head is None:
            print("The Linked List is empty")
            return
        
        # Go to the last node
        itr = self.head
        while itr.next:
            itr = itr.next
        
        # Traverse backward
        llist = ''
        while itr:
            llist += str(itr.data) + ' '
            itr = itr.prev
        
        print(llist)
