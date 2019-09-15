class Node:
    def __init__(self,data = None):
        self.val = data
        self.next = None
        
        
class Ring:
    def __init__(self):
        self.head = None

def __str__(self):
    ret_str = '['
    temp = self.head
    while temp is not None:
        ret_str+= str(temp.val) + ', '
        temp = temp.next
        if temp == self.head:
            break
    ret_str = ret_str.rstrip(', ')
    ret_str += ']'
        
    return ret_str
Ring.__str__=__str__

def get_last(self):
    if self.head is None:
        return None
    
    temp = self.head.next
    while temp.next!=self.head:
        temp = temp.next
        
    return temp
Ring.get_last = get_last

def insert(self,index,val):
    new_node = Node(val)
    last = self.get_last()
    if index == 0:
        new_node.next = self.head
        self.head = new_node
        
        if last is None:
            self.head.next = self.head
        else:
            last.next = new_node
        return
        
    if self.head is None:
        raise IndexError("cannot insert at " + str(index) +"bcz list is empty")
        
    temp = self.head
    counter = 0
    while temp is not None and counter < index:
        prev = temp
        temp = temp.next
        counter+=1
        
    prev.next = new_node
    new_node.next = temp
Ring.insert = insert

def remove(self,val):
    if self.head is None:
        return 
    temp = self.head
    last = self.get_last()
    if temp.val == val:
        if last == self.head:
            self.head = None
        else:
            self.head = temp.next
            last.next = self.head
    prev = temp
    temp = temp.next
    while temp!=self.head:
        if temp.val == val:
            break
        prev = temp
        temp = temp.next
    if temp == self.head:
        return
    prev.next = temp.next # losing reference
Ring.remove = remove

def len(self):
    temp = self.head
    if self.head is None:
        return 0
    if self.head.next is None:
        return 1
    last = self.get_last()
    counter = 1
    while temp!=last:
        temp = temp.next
        counter = counter + 1
    return counter
Ring.len = len

def remove_at(self,index):
    temp = self.head
    last = self.get_last()
    if index==0:
        if last == self.head:
            self.head = None
        elif self.head == temp.next:
             last.next = self.head
        else:
            self.head = temp.next.next
            last.next = self.head
        return 
        
    counter = 2
    temp = self.head
    prev = temp
    temp=temp.next
    while    counter<index:
        prev = temp
        temp = temp.next
        counter = counter + 1
        
    prev.next = temp.next
        
Ring.remove_at = remove_at

def get(self,index):
    if self.head is None:
        raise IndexError("IndexError: Index out of bound")
    temp = self.head
    counter = 0
    while temp is not None and counter <= index:
        if index == counter:
            return temp.val
        temp = temp.next
        counter = counter + 1
Ring.get = get

def push(self,val):
    index = self.len()
    self.insert(index,val)
Ring.push = push

def pop(self):
    index = self.len()-1
    get = self.get(index)
    remove = self.remove_at(index)
    return get
    
Ring.pop = pop
    

if __name__ == '__main__': 
    r = Ring()
    r.insert(1, 1)
    r.insert(0, 1)
    r.insert(0, 2)
    r.insert(1, 3)
    r.insert(7, 5)  # different behavrior since it's a ring! 
    print(r)
