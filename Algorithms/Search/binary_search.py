class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if not root:
            return TreeNode(key)
        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        elif key > root.key:
            root.right = self._insert_recursive(root.right, key)
        return root

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if not root or root.key == key:
            return root
        if key < root.key:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        if not root:
            return root
        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            root.key = self._find_min(root.right)
            root.right = self._delete_recursive(root.right, root.key)
        return root

    def _find_min(self, root):
        while root.left:
            root = root.left
        return root.key

    def inorder_traversal(self):
        result = []
        self._inorder_traversal_recursive(self.root, result)
        return result

    def _inorder_traversal_recursive(self, root, result):
        if root:
            self._inorder_traversal_recursive(root.left, result)
            result.append(root.key)
            self._inorder_traversal_recursive(root.right, result)


# Example usage:
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(8)
    bst.insert(1)
    bst.insert(4)
    bst.insert(7)
    bst.insert(9)

    print("Inorder Traversal:", bst.inorder_traversal())
    print("Search for 4:", bst.search(4) is not None)
    print("Search for 6:", bst.search(6) is not None)

    bst.delete(3)
    print("Inorder Traversal after deleting 3:", bst.inorder_traversal())
