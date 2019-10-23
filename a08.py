class HashMap:
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size
def _get_Hash(self,key):
    if key == str(key):
        return len(key) % self.size
    if type(key) is tuple:
        return key[1]%self.size

    else:
        return key % self.size
HashMap._get_Hash=_get_Hash
def add(self,key,value):
    key_hash = self._get_Hash(key)
    key_value = [key,value]
    
    self.map[key_hash] = [key_value]
    return True
HashMap.add = add
def get(self,key):
    key_hash = self._get_Hash(key)
    if self.map[key_hash] is not None:
        for pair in self.map[key_hash]:
            if pair[0] == key:
                return pair[1]
    else:
        raise KeyError(str(key))
HashMap.get = get
def __str__(self):
    ret = ""
    for i , item in enumerate(self.map):
        if item is not None:
            ret+= str(i) + " : " + str(item) + '\n'
    return ret
HashMap.__str__=__str__
def delete(self,key):
    key_hash = self._get_Hash(key)
    if self.map[key_hash] is None:
        raise KeyError(str(key))
    for i in range(0,len(self.map[key_hash])):
        if self.map[key_hash][i][0]==key:
            self.map[key_hash].pop(i)
            return True
HashMap.delete = delete


if __name__ == '__main__': 
    h = HashMap() 

    h.add(17, "seventeen")
    h.add(26, "twenty six")
    h.add(35, "thirty five")
    h.add(25, "twenty five")
    h.add(26, "twenty six updated")
    h.add(887, "large number")

    print(h)
