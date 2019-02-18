from stack import Stack

class SyntaxChecker:
    def __init__(self):
        self.stack = Stack()
    def check_syntax(self,string):
        for char in string:
            if(char == '{' or char == '(' or char == '['):
                self.stack.push(char)
            elif(char == '}' or char == ')' or char == ']'):
                top_object = self.stack.pop()
                top_object = top_object.data
                if(char == '}' and top_object is not '{'):
                    print("Syntax Error")
                    return False
                elif(char == ')' and top_object is not '('):
                    print(char,top_object)
                    print("Syntax Error")
                    return False
                elif(char == ']' and top_object is not '['):
                    print("Syntax Error")
                    return False
                
        if self.stack.is_empty():
            print("Valid Syntax")
            return True
        print("Syntax Error")
        return False
                
                

def main():
    checker = SyntaxChecker()
    checker.check_syntax('{((shubham gupta))')

main()
