class Set:
    # Constructor
    # @@Param list of elements
    def __init__(self, elements):
        self.sets = [None]*(len(elements)+1)
        for element in elements:
            self.sets[element] = -1

    def __str__(self):
        return str(self.sets)

    # Method to find the parent of the element
    # @@Param: element

    def find(self, element):
        if self.sets[element] < 0:
            return element
        return self.find(self.sets[element])

    # Method to take union of two sets
    # @@Param: first_element, second_element
    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent != y_parent:
            if self.sets[x_parent] < self.sets[y_parent]:
                self.sets[y_parent] = x_parent
                self.sets[x_parent] -= 1
            else:
                self.sets[x_parent] = y_parent
                self.sets[y_parent] -= 1


def main():
    dset = Set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(dset)
    dset.union(1, 2)
    print(dset)
    dset.union(2, 3)
    print(dset)
    dset.union(1, 7)
    print(dset)


main()
