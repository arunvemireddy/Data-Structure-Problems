class HuffmanNode:
    def __init__(self, char, count):
        self.char = char
        self.count = count
        self.left = None
        self.right = None
    
    def __add__(self,other):
        new_node = HuffmanNode(None,self.count+other.count)
        new_node.left = self
        new_node.right = other
        return new_node

    def __str__(self):
        return str(self.char)+" "+str(self.count)

class HuffmanCode:
    def __init__(self,string):
        if not isinstance(string, str):
            raise ValueError("Invalid string")
        self.string = string
        self.root = None
        self.array = self.__construct_array(string)
        
    
    def __construct_array(self,string):
        table = {}
        ret_value = []
        for char in string:
            if char in table:
                table[char] +=1
            else:
                table[char] = 1
        print(table)
        for key in table:
            node = HuffmanNode(key,table[key])
            ret_value.append(node)
        return ret_value
    
    def find_minimum(self):
        self.stack = []
        self.stack.append({"index":0,"object":self.array[0]})
        for index,node in enumerate(self.array):
            if node.count <=self.stack[-1]["object"].count:
                self.stack.append({"index":index,"object":node})
        first = self.stack.pop()
        second = self.stack.pop()
        return first, second

    def construct(self):

        while len(self.array) > 1:
            first,second = self.find_minimum()
            self.array.pop(first["index"])
            self.array.pop(second["index"])
            self.array.append(first["object"]+second["object"])
        print("done")
        print(len(self.array))
        print(self.array[0].left)

    def debug(self,first = None,second = None):
        print('-----------------')
        print("Length: {}".format(len(self.array)))
        if first and second:
            print("xxxxxxxxx:")
            print("ID: {} Node: {}".format(id(first),first))
            print("ID: {} Node: {}".format(id(second),second))
            print("xxxxxxxxx:")
        for node in self.array:
            print("ID: {} Node: {}".format(id(node),node))
        print("-----------------")



def main():
    code = HuffmanCode("sdjflihoilsjdvbowehouwef")
    code.construct()

main()