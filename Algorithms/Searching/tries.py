
# Class to represent one Trie Node
class TrieNode:
    # Constructor
    # @@Param: char
    def __init__(self,char):
        self.char = char
        self.children = {}
        self.end_of_string = False

# Class for Tries
class Tries:
    # Constructor
    def __init__(self):
        self.root = TrieNode(None)

    # Method to insert a word in a trie
    # @@Param: string to insert, optional param to true if you want to search
    def insert_word(self,string,search=False):
        if not isinstance(string, str):
            raise ValueError("Invalid string")
        
        if string[0] not in self.root.children:                 # As the root node is Null pointer insert into children
            if search:                                          # If search is triggered insted of insert
                return False
            self.root.children[string[0]] = TrieNode(string[0]) # Insert a new trie node in the root's hash table
                
        current_node = self.root.children[string[0]]
            
        for char in string[1:]:                                 # Loop through all the chars to insert or search into trie
            if char not in current_node.children:
                if search:
                    return False
                current_node.children[char] = TrieNode(char)
                
            current_node = current_node.children[char]
        
        if search:
            return True
        current_node.end_of_string = True
    
    # Method to search into if the word exists
    # @@Param: string to search
    def search(self,string):
        return self.insert_word(string,search=True)


def main():
    trie = Tries()
    trie.insert_word("shubham")
    trie.insert_word("shubhamgh")
    trie.insert_word("shubhamg")
    print(trie.search("sello"))

main()