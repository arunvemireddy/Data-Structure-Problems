class BloomFilter:
    def __init__(self,depth=1,length=19):
        self.data = [[False]*length for i in range(depth)]
        self.depth = depth
        self.length = length
        self.hashes = {
            "first":lambda string: sum([ord(char)*(266**index) for index,char in enumerate(list(string[::-1]))])%self.length,
            "second":lambda string: sum([ord(char) for char in list(string)])%self.length
        }
    
    def __str__(self):
        ret_value = ""
        for current_filter in self.data:
            ret_value += str(current_filter) + "\n"
        return ret_value

        

    def search(self, string):
        ret_value = False
        counter = 0
        indices = [self.hashes[func](string) for func in self.hashes ]
        for index, row in enumerate(self.data):
            if index != counter:
                break
            for index in indices:
                if row[index]:
                    continue
                else:
                    for ind in indices:
                        row[ind] = True
                    break
            else:
                counter +=1
                ret_value = True
        return counter

def main():
    bloom_filter = BloomFilter(depth=1)
    bloom_filter.search("shubham")
    bloom_filter.search("algorithm")
    bloom_filter.search("shubham")
    print(bloom_filter.search("mahbuhs"))

main()
