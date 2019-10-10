class Person:
    def __init__(self,name,age,queue_num):
        self.name = name
        self.age = age
        self.queue_num = queue_num
    def get_priority(self):
        if self.age >= 40:
            return (100 - self.queue_num) + 100
        else:
            return  (100 - (self.queue_num))
    def __str__(self):
        return str(self.name) + " " + str(self.get_priority())



def heapify(lst,n,root):
    largest = root
    l = 2*root + 1
    r = 2*root + 2
    if  l < n  and lst[l].get_priority() < lst[largest].get_priority():
        largest = l
    if r < n and lst[r].get_priority() < lst[largest].get_priority():
        largest = r
    if largest!=root:
        lst[root] , lst[largest] = lst[largest] ,lst[root]
        
        heapify(lst,n,largest)


def build_heap(lst):
    n = len(lst)
    for i in reversed(range(n//2)):
        heapify(lst,n,i)

def heap_sort(lst):
    n = len(lst)
    
    build_heap(lst)
    
    for i in reversed(range((n))):
        lst[i] , lst[0] = lst[0],lst[i]
        
        heapify(lst,i,0)





if __name__ == '__main__': 
    p = Person('A', 24, 1) 
    print(p) # should output: A 99

    p = Person('A', 40, 1) 
    print(p) # should output: A 199
    
    people = [ 
        Person('A', 24, 1), 
        Person('B', 32, 2), 
        Person('C', 45, 3), 
        Person('D', 22, 4), 
        Person('E', 21, 5), 
        Person('F', 32, 6), 
        Person('G', 39, 7), 
        Person('H', 44, 8), 
        Person('I', 22, 9), 
        Person('J', 29, 10), 
        Person('K', 32, 11), 
        Person('L', 31, 12) 
    ]
    
    print([str(p)  for p in people])
    heap_sort(people) 
    print([str(p)  for p in people])
    # sould output: 
    # ['C 197', 'H 192', 'A 99', 'B 98', 'D 96', 'E 95', 'F 94', 'G 93', 'I 91', 'J 90', 'K 89', 'L 88']
