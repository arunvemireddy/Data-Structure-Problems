# Tree node
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

# Huffman Code Class helps creating 
class HuffmanCode:
    # Constructor
    # @@Param: String on which to perform huffman codeing
    def __init__(self,string):
        if not isinstance(string, str):
            raise ValueError("Invalid string")
        self.string = string
        self.root = None
        self.array = self.__construct_tree_array(string)
        self.table = {}
    
    # Method to create tree array
    # @@Param string
    def __construct_tree_array(self,string):
        table = {}
        ret_value = []
        for char in string:                     # For each char in string
            if char in table:                   # Check if present in hashtable
                table[char] +=1                 # If key is present increment counter
            else:
                table[char] = 1                 # else set to one
        for key in table:
            node = HuffmanNode(key,table[key])      # Create Huffman tree node corrospointing to each key in table
            ret_value.append(node)
        return ret_value
    

    # We should use priority queue for this
    # Method to find last 2 minimum counter 
    def find_minimum(self):
        self.stack = []
        self.stack.append({"index":0,"object":self.array[0]})
        for index,node in enumerate(self.array):
            if node.count <=self.stack[-1]["object"].count:
                self.stack.append({"index":index,"object":node})
        first = self.stack.pop()
        second = self.stack.pop()
        return first, second

    # Method to construct the huffman tree
    def construct_tree(self):
        while len(self.array) > 1:
            first,second = self.find_minimum()
            self.array.pop(first["index"])
            self.array.pop(second["index"])
            self.array.append(first["object"]+second["object"])

        self.root = self.array[0]

    # Method to convert a huffman tree to code
    def construct_code(self,path,node):
        if not node:
            return
        if node.left is None and node.right is None:                                # If leaf node
            self.table[node.char] = ''.join([str(element) for element in path])     # Add the path to table
            return

        if node.left:
            path.append(0)                              # Append 0 if going left
            self.construct_code(path[:],node.left)
        if node.right:
            path.append(1)                              # Append 1 to path if going right
            self.construct_code(path[:],node.right)

    # Method to print the code
    def print_table(self):
        for key in self.table:
            print("{}: {}".format(key, self.table[key]))


    # Method to debug
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

# Driver Code
def main():
    code = HuffmanCode("sdjflihoilsjdvbowehouwef")
    code.construct_tree()
    code.construct_code([],code.root)
    code.print_table()
main()