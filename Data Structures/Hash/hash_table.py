# This is an implementation of a hash table, which is a data structure that
# stores data in key-value pairs. This implementation is a hash table with
# chaining, which means that if there is a collision, the data will be stored

# Other forms of hash tables include hash sets, which only store values, and
# hash maps, which are the same as hash tables but not synchornized, meaning
# that they are not thread safe

class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def _hash(self, key):
        '''
        This is a private method that is only used within the class,
        this function will return the hash of the key by using the
        ASCII value of the key and multiplying it by the index of the
        key in the string
        '''
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % self.size
        return hash

    def set(self, key, value):
        '''
        This function will set the value of the key in the hash table
        '''
        hash = self._hash(key)
        if not self.data[hash]:
            self.data[hash] = []
        self.data[hash].append([key, value])
        return self.data

    def get(self, key):
        hash = self._hash(key)
        if self.data[hash]:
            for i in range(len(self.data[hash])):
                if self.data[hash][i][0] == key:
                    return self.data[hash][i][1]
        return None

    def keys(self):
        keys = []
        for i in range(self.size):
            if self.data[i]:
                for j in range(len(self.data[i])):
                    keys.append(self.data[i][j][0])
        return keys

    def values(self):
        values = []
        for i in range(self.size):
            if self.data[i]:
                for j in range(len(self.data[i])):
                    values.append(self.data[i][j][1])
        return values

    def entries(self):
        entries = []
        for i in range(self.size):
            if self.data[i]:
                for j in range(len(self.data[i])):
                    entries.append(self.data[i][j])
        return entries

    def delete(self, key):
        hash = self._hash(key)
        if self.data[hash]:
            for i in range(len(self.data[hash])):
                if self.data[hash][i][0] == key:
                    print(f'deleting {self.data[hash][i]}')
                    self.data[hash].pop(i)
                    return
        return False


if __name__ == "__main__":
    hash_table = HashTable(50)
    hash_table.set("grapes", 10000)
    hash_table.set("apples", 54)
    hash_table.set("oranges", 2)
    hash_table.set("bananas", 10)
    print(hash_table.get("grapes"))
    print(hash_table.keys())
    print(hash_table.values())
    print(hash_table.entries())
    hash_table.delete("apples")

    print(hash_table.get("apples"))
    print(hash_table.keys())
    print(hash_table.values())
    print(hash_table.entries())
