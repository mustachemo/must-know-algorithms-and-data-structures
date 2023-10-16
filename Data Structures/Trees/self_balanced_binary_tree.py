# 'TreeNode represents a node in the AVL tree. Each node has a key attribute to store the node's value, left and right attributes to point to the left and right children, and a height attribute to store the height of the node.

# AVLTree represents the balanced binary tree (AVL tree). It has methods for inserting nodes and includes helper functions for balancing and performing rotations as needed to maintain the AVL tree's balance.

# The _balance function calculates the balance factor of a node, which is the difference between the heights of its left and right subtrees.

# The _right_rotate and _left_rotate functions perform right and left rotations, respectively, to rebalance the tree.

# The _insert function inserts a key into the AVL tree while ensuring that the tree remains balanced.'

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Height of the node, initialized to 1


class AVLTree:
    def __init__(self):
        self.root = None

    # Helper function to get the height of a node
    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    # Helper function to balance a node and update its height
    def _balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    # Helper function to perform a right rotation
    def _right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))

        return x

    # Helper function to perform a left rotation
    def _left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    # Helper function to insert a key into the AVL tree
    def _insert(self, node, key):
        if not node:
            return TreeNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        # Update height of current node
        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))

        # Perform balancing
        balance = self._balance(node)

        # Left Heavy
        if balance > 1:
            if key < node.left.key:
                return self._right_rotate(node)
            else:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)

        # Right Heavy
        if balance < -1:
            if key > node.right.key:
                return self._left_rotate(node)
            else:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)

        return node

    # Public function to insert a key into the AVL tree
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def visualize(self):
        def _visualize_tree(node, level=0, prefix="Root: "):
            if node is not None:
                if level == 0:
                    print(prefix + str(node.key))
                else:
                    print(" " * (level - 1) * 4 +
                          prefix + "|__ " + str(node.key))
                if node.left is not None or node.right is not None:
                    if node.left:
                        left_prefix = "|"
                        if node.right:
                            left_prefix += "   "
                        else:
                            left_prefix += "__ "
                        _visualize_tree(node.left, level + 1, left_prefix)
                    if node.right:
                        _visualize_tree(node.right, level + 1, "`__ ")

        if self.root is not None:
            _visualize_tree(self.root)
        else:
            print("The tree is empty.")


# Example usage:
if __name__ == "__main__":
    avl_tree = AVLTree()
    keys = [9, 5, 10, 0, 6, 11, -1, 1, 2]
    for key in keys:
        avl_tree.insert(key)

    avl_tree.visualize()
