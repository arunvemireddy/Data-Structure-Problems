# Class which demonstrates working of a Hashtable
class HashTable:
    # Constructor
    # @@Param: type of probing['linear','quad', 'double hashing']
    def __init__(self,probing='linear'):
        self.data = [None]*5
        self.length = len(self.data)
        self.filled = 0
        self.keys = []

        self.prob_function = {
            "linear":lambda x,y=0: ((x+1) % self.length,y),
            "quadratic":lambda x,y: ((x+y)**2 % self.length,y+1),
            "double-hashing":None
        }
        
        if probing not in self.prob_function:
            raise ValueError("Invalid Probing types must be linear,quadratic or double-hashing")
        self.prob_type = probing

    # Pseudoprivate Method to find the hash of the key
    # @@Params: KEY
    def __hash(self,key):
        if len(key) == 0:
            raise ValueError("Invalid key")
        total = 0
        for char in key:
            total += ord(char)
        return total%self.length
    
    # Method to insert a new value into hashtable
    # @@Params: KEY and VALUE
    def insert(self,key,value):
        index = self.__hash(key)
        if self.filled >= self.length:
            self.expand()
        self.keys.append(key)
        final_index = self.prob(index,0)
        self.data[final_index] = (key,value)
        self.filled +=1

    # Method to do linear probing
    # @@Params: index, probing factor, data
    def prob(self,index,factor=0):
        if (self.data[index + factor] == False) or (self.data[index+factor]== None):
            return index+factor
        next_index, next_factor = self.prob_function[self.prob_type](index, factor) 
        return self.prob(next_index,next_factor)

    
    
    # Method to search for a key value
    # @@Param: Key 
    def search(self,key):
        if key not in self.keys:
            raise ValueError("Invalid key")
        index = self.__hash(key)
        factor = 0
        while self.data[index] != False and self.data[index][0] != key:
            index,factor = self.prob_function[self.prob_type](index, factor)
        return self.data[index][1]

    # Method to delete a key from the hashtable
    # @@Params: key
    def delete(self,key):
        index = self.__hash(key)
        if not key in self.keys:
            raise ValueError("Invalid Key")
        factor = 0
        while (self.data[index] and self.data[index][0] == key) or (self.data[index] == False):
            index,factor = self.prob_function[self.prob_type](index, factor)
        self.data[index] = False
        self.filled -=1
        if len(self.data)//4 == self.filled:
            self.shrink()
    

    # Method to perform table doubling
    def expand(self):
        new_list = [None]*(2*self.length)
        temp = self.data
        self.data = new_list
        self.length = len(self.data)
        self.filled = 0
        for index,entry in enumerate(temp):
            if entry:
                self.insert(entry[0],entry[1])
                
    
    # Method to shrink the array 
    def shrink(self):
        if not self.filled <= self.length//4:
            return
        new_list = [None]*(self.length//2)
        temp = self.data
        self.data = new_list
        self.length = len(self.data)
        self.filled = 0
        for entry in temp:
            if entry:
                self.insert(entry[0],entry[1])

    def __str__(self):
        return str(self.data)

def main():
    table = HashTable(probing="linear")
    print(table.filled)
    values = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
    for i in range(15):
        table.insert(values[i],i)
    print(table)
    for i in range(10):
        table.delete(values[i])
    print(table)

main()