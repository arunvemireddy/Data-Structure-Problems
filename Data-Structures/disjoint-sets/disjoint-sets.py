class Set:
    def __init__(self,elements):
        self.sets = [None]*(len(elements)+1)
        for element in elements:
            self.sets[element] = element
            

    def __str__(self):
        return str(self.sets)

def main():
    dset = Set([1,2,3,4])
    print(dset)
main()
        
    