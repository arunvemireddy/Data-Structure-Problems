class HashTable:
    def __init__(self):
        self.data = [None]*11
        self.length = 11
        self.filled = 0
        self.keys = []
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
            raise ValueError("Hash Table is Full")
        self.keys.append(key)
        self.prob(index,0,(key,value))
        self.filled +=1

    def prob(self,index,factor,data):
        if not self.data[index+factor]:
            self.data[index+factor] = data
            return True
        self.prob(index,factor+1,data)
    def search(self,key):
        if key not in self.keys:
            raise ValueError("Invalid key")
        index = self.__hash(key)
        while self.data[index][0] != key:
            index +=1
        return self.data[index][1]

    def __str__(self):
        return str(self.data)
def main():
    table = HashTable()
    table.insert("shubham",23)
    table.insert("gupta",25)
    table.insert("shikha",98)
    table.insert("aditya",10)
    table.insert("ayushi",89)
    table.insert("arushi",98)
    print(table)
    print(table.search("shubham"))
main()