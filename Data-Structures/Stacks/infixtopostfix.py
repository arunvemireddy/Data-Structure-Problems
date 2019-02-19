from stack import Stack

class InfixToPostFix:
    def __init__(self):
        self.stack = Stack()
        
    def is_operator(self,char):
        operators = {"+","-","/","*"}
        return char in operators
    def is_bracket(self,char):
        brackets = {"(",")"}
        return char in brackets
    def is_operand(self,char):
        operators = {"+","-","/","*",")","("}
        return char not in operators 
    def is_higher_pro(self,first,second):
        priority = {
            "(":17,
            ")":17,
            "[":17,
            "]":17,
            "*":15,
            "/":15,
            "%":15,
            "+":12,
            "-":12
            }
        if first in priority and second in priority:
            return priority[first] >= priority[second]
        return False
    
    def convert(self,expression):
        for char in expression:
            if self.is_operand(char):
                print(char),
            elif char == ")":
                while self.stack.get_top() != "(":
                        top = self.stack.pop().data
                        if not self.is_bracket(char):
                            print(top),
                if self.stack.get_top() == "(":
                    self.stack.pop()
            else:
                if not self.stack.is_empty():
                    if char == ")":
                        pass
                    elif not self.is_higher_pro(char,self.stack.get_top()):
                        top = self.stack.pop().data
                        print(top),
                self.stack.push(char)
                
        while not self.stack.is_empty():
             top = self.stack.pop().data
             print(top),

def main():
    convertor = InfixToPostFix()
    convertor.convert("(A+B)+(C-D)")
                
            
main()
