
# Class to represent one Tree Node
class TreeNode:
    # Constructor
    # @@Param: char
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.children = {}

class SuffixTree:
    def __init__(self,string):
        if not isinstance(string,str):
            raise ValueError("Type should be string")
        

        self.string = string+"$"
        self.suffix = self.__create_suffix(self.string)
        self.root = TreeNode(None,None)
    
    # Method to create all suffix
    # @@Param: string
    def __create_suffix(self,string):
        ret_value = []
        for i in range(len(string)):
            ret_value.append(string[i:])
        ret_value.sort()
        return ret_value

SuffixTree("banana")
    
