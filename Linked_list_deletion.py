class node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class linked:
    def __init__(self):
        self.head=None
        
    def  print_ll(self):
        if self.head is None:
            print("ll is empty") 
        else:
            n=self.head     
            while n is not None:
                print(n.data,end=" ")
                n=n.ref
    def add_beg(self,data):
        new_node=node(data) 
        new_node.ref=self.head
        self.head=new_node 

    def add_end(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node  
    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            else:
               n=n.ref
        if n is None:
            print("item is not present") 
        else:
            new_node=node(data)
            new_node.ref=n.ref
            n.ref=new_node
    def add_before(self,data,x):
        if self.head is None:
            print("Linke  list is empty")
            return
        if self.head.data==x:
            new_node=node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        n=self.head
        while n is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is None:
            print("node is not found")
        else:
            new_node=node(data)
            new_node.ref=n.ref
            n.ref=new_node

    def delete_begin(self):
        if self.head is None:
            print("ll is empty")
        else:
            self.head=self.head.ref

    def delete_end(self):
        if self.head is None:
            print("ll is empty we cant delete node")
        elif self.head.ref is None:
             self.head=None 
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None    
    def delete_by_value(self,x):
        if self.head is None:
            print("ll is empty")
        elif x==self.head.data:
            self.head=self.head.ref
        n=self.head  
        while n.ref is not None:
            if x==n.ref.data:
                break
            n=n.ref
        if n.ref is None:
            print("node is not preset")
        else:
            n.ref=n.ref.ref







a=linked()
a.add_beg(44)
a.add_end(55)
a.add_after(45,44)
a.add_beg(77)
a.add_before(85,77)

a.delete_by_value(77)
a.print_ll()                


