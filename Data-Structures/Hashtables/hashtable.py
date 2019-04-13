class HashTable:
    def __init__(self,probing='linear'):
        self.data = [None]*11
        self.length = 11
        self.filled = 0
        self.keys = []
        self.probing = probing
    def __hash(self,key):
        if len(key) == 0:
            raise ValueError("Invalid key")
        total = 0
        for char in key:
            total += ord(char)
        return total%self.length
    
    def insert(self,key,value):
        index = self.__hash(key)
        if self.filled == self.length:
            print("extanding")
            self.expand()
        self.keys.append(key)
        self.prob(index,0,(key,value))
        self.filled +=1

    def prob(self,index,factor,data):
        if not self.data[index+factor]:
            self.data[index+factor] = data
            return True
        self.prob
        (index,factor+1,data)

    def quad_prob(self,index,factor,data):
        if not self.data[index+factor]:
            self.data[index+factor] = data
            return True
        self.prob(index,(factor+1)**2,data)
    

    def search(self,key):
        if key not in self.keys:
            raise ValueError("Invalid key")
        index = self.__hash(key)
        while self.data[index][0] != key:
            index +=1
        return self.data[index][1]

    def delete(self,key):
        pass

    def expand(self):
        new_list = [None]*(2*self.length)
        temp = self.data
        self.data = new_list
        self.length = len(self.data)
        for entry in temp:
            if entry:
                self.insert(entry[0],entry[1])
    
    def shrink(self):
        if not self.filled <= self.length//4:
            return
        new_list = [None]*(self.length//2)
        temp = self.data
        self.data = new_list
        self.length = len(self.data)
        for entry in temp:
            if entry:
                self.insert(entry[0],entry[1])


    def __str__(self):
        return str(self.data)
def main():
    table = HashTable()
    values = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
    for i in range(15):
        print(i)
        table.insert(values[i],i)
    print(table)
main()