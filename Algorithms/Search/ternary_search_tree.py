# A ternary search tree (TST) is a type of tree data structure that
# combines the properties of binary search trees and tries. It allows
# for efficient insertion, deletion, and searching of keys that are strings
# or sequences. Here's a basic implementation of a ternary search tree in Python:

# TSTNode represents a node in the ternary search tree. Each node stores a character (char) and has three child pointers: left, middle, and right. Additionally, it can hold an optional value associated with the node.

# TernarySearchTree represents the ternary search tree. It has a root attribute pointing to the root node.

# The insert method inserts a key (a string) into the TST with an optional associated value.

# The _insert method is a recursive helper function for inserting a key into the tree.

# The search method searches for a key in the TST and returns its associated value if found, or None otherwise.

# The _search method is a recursive helper function for searching a key in the tree.

class TSTNode:
    def __init__(self, char):
        self.char = char  # Character stored in this node
        self.left = None  # Left subtree
        self.middle = None  # Middle subtree
        self.right = None  # Right subtree
        self.value = None  # Value associated with the node (optional)


class TernarySearchTree:
    def __init__(self):
        self.root = None  # Root node of the TST

    def insert(self, key, value=None):
        self.root = self._insert(self.root, key, value, 0)

    def _insert(self, node, key, value, index):
        char = key[index]

        if node is None:
            node = TSTNode(char)

        if char < node.char:
            node.left = self._insert(node.left, key, value, index)
        elif char > node.char:
            node.right = self._insert(node.right, key, value, index)
        elif index < len(key) - 1:
            node.middle = self._insert(node.middle, key, value, index + 1)
        else:
            node.value = value

        return node

    def search(self, key):
        node = self._search(self.root, key, 0)
        return node.value if node else None

    def _search(self, node, key, index):
        if node is None:
            return None

        char = key[index]

        if char < node.char:
            return self._search(node.left, key, index)
        elif char > node.char:
            return self._search(node.right, key, index)
        elif index < len(key) - 1:
            return self._search(node.middle, key, index + 1)
        else:
            return node


# Example usage:
if __name__ == "__main__":
    tst = TernarySearchTree()

    tst.insert("apple", 5)
    tst.insert("banana", 10)
    tst.insert("cherry", 15)

    print("Search for 'apple':", tst.search("apple"))  # Should print 5
    print("Search for 'banana':", tst.search("banana"))  # Should print 10
    print("Search for 'cherry':", tst.search("cherry"))  # Should print 15
    print("Search for 'grape':", tst.search("grape"))  # Should print None
