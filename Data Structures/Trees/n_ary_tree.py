# An n-ary tree is a tree data structure in which each node can have at most n children.
# Here's a basic implementation of an n-ary tree in Python:

class NaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []


class NaryTree:
    def __init__(self, root_value):
        self.root = NaryTreeNode(root_value)

    def add_child(self, parent, child_value):
        child = NaryTreeNode(child_value)
        parent.children.append(child)

    def visualize(self):
        def print_node(node, level):
            if level > 0:
                print("  " * (level - 1) + "  |")
            print("  " * level + "  " + str(node.value))
            for i, child in enumerate(node.children):
                print_node(child, level + 1)
                if i < len(node.children) - 1:
                    print("  " * (level + 1) + "  |")

        if self.root is not None:
            print_node(self.root, 0)
        else:
            print("The tree is empty.")


# Example usage:
if __name__ == "__main__":
    nary_tree = NaryTree(0)

    nary_tree.add_child(nary_tree.root, 1)
    nary_tree.add_child(nary_tree.root, 2)
    nary_tree.add_child(nary_tree.root, 3)

    nary_tree.add_child(nary_tree.root.children[0], 4)
    nary_tree.add_child(nary_tree.root.children[0], 5)

    nary_tree.add_child(nary_tree.root.children[2], 6)
    nary_tree.add_child(nary_tree.root.children[2], 7)
    nary_tree.add_child(nary_tree.root.children[2], 8)

    nary_tree.add_child(nary_tree.root.children[2].children[2], 9)

    print("Visualized N-ary Tree:")
    nary_tree.visualize()

    # Visualized N-ary Tree:
    #               0
    #             / | \
    #            /  |  \
    #           1   2   3
    #          / \    / | \
    #         4   5  6  7  8
    #                   |
    #                   9
