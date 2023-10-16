class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_data):
        self.root = Node(root_data)

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursive(current_node.left, data)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursive(current_node.right, data)

    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, current_node, data):
        if current_node is None:
            return False
        if current_node.data == data:
            return True
        elif data < current_node.data:
            return self._search_recursive(current_node.left, data)
        else:
            return self._search_recursive(current_node.right, data)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal_recursive(self.root, result)
        return result

    def _inorder_traversal_recursive(self, current_node, result):
        if current_node:
            self._inorder_traversal_recursive(current_node.left, result)
            result.append(current_node.data)
            self._inorder_traversal_recursive(current_node.right, result)


# Example usage:
if __name__ == "__main__":
    tree = BinaryTree(5)
    tree.insert(3)
    tree.insert(8)
    tree.insert(1)
    tree.insert(4)
    tree.insert(7)
    tree.insert(9)

    print("Inorder Traversal:", tree.inorder_traversal())
    print("Search for 4:", tree.search(4))
    print("Search for 6:", tree.search(6))
