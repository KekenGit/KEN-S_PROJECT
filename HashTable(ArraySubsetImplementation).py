class HashTable:

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):

        index = self.hash_function(key)

        if key not in self.table[index]:
            self.table[index].append(key)

    def display(self):

        for i in range(self.size):
            print("Index", i, ":", self.table[i])

size = int(input("Enter hash table size: "))

ht = HashTable(size)

values = list(map(int, input("Enter values: ").split()))

for val in values:
    ht.insert(val)

ht.display()