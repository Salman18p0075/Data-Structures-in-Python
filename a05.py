class Node:
    def __init__(self,data = None):
        self.val = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

def push(self,val):
    new_node = Node(val)
    if self.head is None:
        self.head = new_node
        return
    last = self.head
    while last.next is not None:
        last = last.next
        
    last.next = new_node
    
LinkedList.push = push

def pop(self):
    if self.head is None:
        raise Exception("cannot pop due to no value")
    
    if self.head.next is None:
        print("case 1")
        val = self.head.val
        self.head = None
        return val
    
    print("case 2")
    temp = self.head
    while temp.next is not None:
        prev = temp
        temp = temp.next
        
    val = temp.val
    prev.next = None
    return val

LinkedList.pop = pop

def __str__(self):
    rstr = "["
    temp = self.head
    while temp is not None:
        rstr+=str(temp.val) + ' ,'
        temp = temp.next
        
    rstr = rstr.rstrip(',')
    rstr += "]"
    return rstr
LinkedList.__str__ = __str__

def insert(self,index,val):
    new_node = Node(val)
    if index == 0:
        new_node.next = self.head
        self.head = new_node
        return 
    
    temp = self.head
    counter = 0
    while temp is not None and counter<index:
        prev = temp
        temp = temp.next
        counter+=1
    prev.next = new_node
    new_node.next = temp

LinkedList.insert = insert

def remove(self,val):
    temp = self.head
    if temp is not None:
        if temp.val==val:
            self.head = temp.next
            temp = None
            return
    while temp is not None:
        if temp.val == val:
            break
        prev = temp
        temp = temp.next
        
    if temp is None:
        return
    
    prev.next = temp.next
LinkedList.remove = remove

def getindex(self,index):
    if index >= self.len1():
        raise Exception( "index out of range")
    counter = 0
    temp = self.head
    while temp is not None:
        if counter == index:
            return temp.val
        temp = temp.next
        counter+=1
        
LinkedList.getindex = getindex

def remove_at(self,index):
    get = self.getindex(index)
    remove = self.remove(get)
        
LinkedList.remove_at = remove_at

def reverse_list(self):
    if self.head is None:
         return None
    if self.head.next is None:
        return None
    prev = None
    temp = self.head
    while temp is not None:
        next = temp.next
        temp.next = prev
        prev = temp
        temp = next
    self.head = prev
LinkedList.reverse_list = reverse_list
        
        


            
    

if __name__ == '__main__': 
    l = LinkedList() 
    l.push(1) 
    l.push(2)
    l.push(3)

    print(l)

    l.reverse_list() 
    print(l)

