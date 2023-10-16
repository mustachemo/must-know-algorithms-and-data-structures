
class Node:
    '''The node in the linked list'''

    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    the array that will hold the linked lists

    '''

    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.size = 0
        # initialize the array with size capacity and all values are None
        self.table = [None] * capacity

    def __str__(self):
        elements = []
        for i in range(self.capacity):
            current = self.table[i]
            while current:
                elements.append((current.key, current.value))
                current = current.next
        return str(elements)

    def _hash(self, key):
        '''hash function'''
        return hash(key) % self.capacity

    def insert(self, key, value):
        '''insert key value pair into hash table'''
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    def remove(self, key):
        '''Remove the value based on the key'''
        index = self._hash(key)

        previous = None
        current = self.table[index]

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current
            current = current.next

        raise KeyError(key)

    def search(self, key):
        '''Search for the value based on the key'''
        index = self._hash(key)

        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
            raise KeyError(key)

    def __len__(self):
        return self.size

    def __contains__(self, key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False


# Driver code
if __name__ == '__main__':

    # Create a hash table with
    # a capacity of 5
    ht = HashTable(5)

    # Add some key-value pairs
    # to the hash table
    ht.insert("apple", 3)
    ht.insert("banana", 2)
    ht.insert("cherry", 5)

    # Check if the hash table
    # contains a key
    print("apple" in ht)  # True
    print("durian" in ht)  # False

    # Get the value for a key
    print(ht.search("banana"))  # 2

    # Update the value for a key
    ht.insert("banana", 4)
    print(ht.search("banana"))  # 4

    ht.remove("apple")
    # Check the size of the hash table
    print(len(ht))  # 3
