# A B-tree is a self-balancing tree data structure that maintains sorted data and
# allows for efficient insertion, deletion, and search operations. Here's a basic
# implementation of a B-tree in Python:

# BTreeNode represents a node in the B-tree. Each node has a list of keys and a list of children. The leaf attribute is used to determine if the node is a leaf node.

# BTree represents the B-tree. It has a root attribute that points to the root node and a degree attribute, which is the minimum degree of the B-tree. The degree determines the maximum number of keys a node can have.

# The insert method inserts a key into the B-tree.

# The _insert_non_full method inserts a key into a non-full node.

# The _split_child method splits a child node when it's full.

# The search method searches for a key in the B-tree.

# The visualize method displays the structure of the B-tree, showing each level and the keys at each level.

class BTreeNode:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []
        self.children = []


class BTree:
    def __init__(self, degree=2):
        self.root = BTreeNode()
        self.degree = degree  # Minimum degree of the B-tree

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.degree) - 1:
            new_root = BTreeNode(leaf=False)
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key)

    def _insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(None)  # Make space for the new key
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.degree) - 1:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def _split_child(self, parent, index):
        degree = self.degree
        child = parent.children[index]
        new_child = BTreeNode(leaf=child.leaf)
        parent.keys.insert(index, child.keys[degree - 1])
        parent.children.insert(index + 1, new_child)

        new_child.keys = child.keys[degree:]
        child.keys = child.keys[:degree - 1]

        if not child.leaf:
            new_child.children = child.children[degree:]
            child.children = child.children[:degree]

    def search(self, key, node=None):
        if node is None:
            node = self.root
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return True
        elif node.leaf:
            return False
        else:
            return self.search(key, node.children[i])

    def visualize(self, node=None, level=0):
        if node is None:
            node = self.root

        print("Level", level, end=": ")
        print(*node.keys)

        if not node.leaf:
            level += 1
            for child in node.children:
                self.visualize(child, level)


# Example usage:
if __name__ == "__main__":
    b_tree = BTree(degree=3)  # Create a B-tree with a minimum degree of 3

    keys = [3, 8, 2, 6, 7, 1, 4, 9, 5]
    for key in keys:
        b_tree.insert(key)

    b_tree.visualize()
    print("Search for 7:", b_tree.search(7))  # Should return True
    print("Search for 10:", b_tree.search(10))  # Should return False
