class BloomFilter:
    def __init__(self,depth=1,length=10):
        self.data = [[False]*length for i in range(depth)]
        self.depth = depth

    def __str__(self):
        ret_value = ""
        for current_filter in self.data:
            ret_value += str(current_filter) + "\n"
        return ret_value

def main():
    bloom_filter = BloomFilter()
    print(bloom_filter)

main()