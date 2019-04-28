from os import listdir
import os
line_of_code = 0
document_line = 0

def create_dir_map(root=".",limiter="|"):

    global line_of_code
    paths = listdir(root)
    string = ""
    for path in paths:
        if path[0] == "." or path[0] == "_" or path.endswith(".txt") or path.endswith(".pdf") or path.endswith(".pyc"):              # Ignoring hidden files or __init__ files
            continue
        string+= limiter+"____ {}".format(path)+"\n"
        next_root = os.path.join(root,path)
        if os.path.isdir(next_root):
            new_limiter = limiter+"    |"
            string += create_dir_map(next_root,new_limiter)
        else:
            if path.endswith(".py") or path.endswith(".js") or path.endswith(".md"):
                with open(os.path.join(root,path),'r') as f:
                    for lines in f:
                        if  
                        line_of_code +=1
    return string

def main():
    structure =  create_dir_map()
    print(structure)
    print(line_of_code)
main()