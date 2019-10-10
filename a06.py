class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # add rest of Tree Node functions here
def dfs(self):
    print(self.val)
    
    if self.left:
        self.left.dfs()
    if self.right:
        self.right.dfs()
TreeNode.dfs = dfs

def dfs_inorder(self):
    if self.left:
        self.left.dfs_inorder()
    print(self.val)
    
    if self.right:
        self.right.dfs_inorder()
TreeNode.dfs_inorder = dfs_inorder

def dfs_postorder(self):
    if self.left:
        self.left.dfs_postorder()
    if self.right:
        self.right.dfs_postorder()
    
    print(self.val)
TreeNode.dfs_postorder = dfs_postorder

def bfs(self):
    lst = [self]
    while lst:
        curr = lst.pop(0)
        print(curr.val)
        if curr.left:
            lst.append(curr.left)
        if curr.right:
            lst.append(curr.right)
TreeNode.bfs = bfs

def dfs_apply(self,fn):
    fn(self)
    if self.left:
        self.left.dfs_apply(fn)
    if self.right:
        self.right.dfs_apply(fn)
TreeNode.dfs_apply = dfs_apply

class Person: 
    def __init__(self,n):
        self.name = n
    def __str__(self):
        return self.name


    
    
class Collector:
    def __init__(self):
        self.lst = []
    
    def process(self,node):
        self.lst.append(str(node.val))
    
    def get_list(self):
        return self.lst
    def reset_list(self):
        return self.lst.clear()
        
        
    





# Add the find_val function here ########## 
def find_val(self, val):
    if self is None:
        return None
    if val == str(self.val):
        return self
    left = find_val(self.left,val)
    right = find_val(self.right,val)
    if left:
        return left
    else:
        return right

        
        
        
    
    
    
TreeNode.find_val = find_val
def find_people_in_hierarchy(self, name):
    
    l = self.find_val(name)
    if l is None:
        raise ValueError("no match")
    
    c= Collector()
    if l.val==name:
        c.process(l)
    l.dfs_apply(c.process)
        
    return c.get_list()
        
    
        
        
        
    
TreeNode.find_people_in_hierarchy=find_people_in_hierarchy
        
        
        
  


if __name__ == "__main__": 
    pass 


    # # Section 1: creating people 
    print("Section 1: ")
    director = Person("Director")
    hod_1 = Person("HoD 1")
    hod_2 = Person("HoD 2")
    faculty_cs_1 = Person("CS 1")
    faculty_cs_2 = Person("CS 2")
    faculty_ee_1 = Person("EE 1")
    faculty_ee_2 = Person("EE 2")
    print(director) # should print: Director 

    # # Section 2: inserting people in the tree 
    print("\nSection 2: ")
    t_d = TreeNode(director)
    t_d.left = TreeNode(hod_1)
    t_d.right = TreeNode(hod_2)

    t_d.left.left = TreeNode(faculty_cs_1)
    t_d.left.right = TreeNode(faculty_cs_2)

    t_d.right.left = TreeNode(faculty_ee_1)
    t_d.right.right = TreeNode(faculty_ee_2)
    t_d.dfs()


    # # Section 3: try find_val individually 
    print("\nSection 3: ")

    node = t_d.find_val("Director")  
    print(node.val)  # should print the string: Director


    node = t_d.find_val("HoD 1")  
    print(node.val)  # should print the string: HoD 1

    node = t_d.find_val("HoD 2")  
    print(node.val)  # should print the string: HoD 2

    node = t_d.find_val("HoD 3")  
    print(node)  # should print the string: None


    # # Section 4: try the collector 
    print("\nSection 4: ")
    c = Collector() 
    t_d.dfs_apply(c.process)
    print(c.get_list()) # should print the list: ['Director', 'HoD 1', 'CS 1', 'CS 2', 'HoD 2', 'EE 1', 'EE 2']


    # # Section 5: find hierarchy 
    print("\nSection 5: ")
    people = t_d.find_people_in_hierarchy("HoD 1")
    print(people)    # Should print the list: ['HoD 1', 'CS 1', 'CS 2']

