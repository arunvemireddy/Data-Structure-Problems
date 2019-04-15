"""
    This file demonstrates the rabin krap string matching algorithm
"""

class RabinKarp:
    def __init__(self,data):
        self.data  = data
    
    def create_hash(self,pattern):
        hash_array = [ord(char)*(256**index) for index,char in enumerate(list(pattern[::-1]))]
        hash_array.reverse()
        return hash_array

    def search(self,pattern):
        pattern_hash = sum(self.create_hash(pattern))
        current_hash = None 
        for i in range(0,len(self.data)-len(pattern)):
            if not current_hash:
                current_hash = self.create_hash(self.data[i:len(pattern)])
                print(current_hash)
            else:
                current_hash.pop(0)
                #print("appending {}".format(self.data[i+len(pattern)-1]))
                current_hash = [element*256 for element in current_hash]
                current_hash.append(ord(self.data[i+len(pattern)-1]))
            if pattern_hash == sum(current_hash):
                print("Pattern Matched")
                break
        else:
            print("not found")
            

            
            

def main():
    algorithm = RabinKarp("""sdlkflsdjflksdjflksdjflksdjf
    sdfklsdlfkjsdlkfjsdf
    sdflksdklfjsldkfjlksdjf
    sdflksdlkfjsdlkfjklsdhshubhams;dfs;dfjlksdfjlksdjflkadjsfuwejlfnsd;fj'asdjf;lasdjf;lweiufoisldvnhowirgegholer
    vliarehifk;wejigerjslk.ghelrnvkljl;mskdvghlqeam;ewajksdv;kigwrjg
    sdlikakdvmj;poqw4fe;dmjfiieam.vwrjiwmal/sfj;wevqaejgqeam';fwkp;vmeqal;'f
    ewlfj;smv;oqefm'qlewolwjf;weamvng;kwejf'lqwaefmk;owgkvne;fjql/mvfliw4jg""")

    algorithm.search("shubham")

main()