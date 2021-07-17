class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    
    def hash(self,key):
        h = 0
        for char in key :
            h += ord(char)
    
        return h % self.MAX
    
    def get(self,key):
        arr_index = self.hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]

    def add(self,key,val):
        h= self.hash(key)
        found=False
        for idx, element in  enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
        if not found:
            self.arr[h].append((key,val))

        return self.arr[h]        

    def contains(self,key):
        h= self.hash(key)
        found=False
        for idx, element in  enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:                
                found = True
            
        return found
                

if __name__ == '__main__':

    t = HashTable()
    t.add('march 6',130)
    print(t.hash('march 6'))
    print(t.contains('march 6'))
    print(t.arr[9])
    print(t.hash('march 17'))
    print(t.contains('march 17'))
    t.add('march 17',130)
    print(t.arr[9])
    print(t.contains('march 17'))
    print(t.get('march 6'))












