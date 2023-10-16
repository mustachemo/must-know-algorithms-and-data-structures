# A Trie (pronounced "try") is a tree-like data structure used for efficient retrieval of strings
# or keys in a dataset. It's often used for tasks like autocomplete and spell checking. Here's a
# basic implementation of a Trie in Python:

# TrieNode represents a node in the Trie. Each node has a children dictionary to store child nodes (corresponding to characters in words) and an is_end_of_word flag to indicate if a complete word ends at that node.

# Trie represents the Trie data structure. It has methods for inserting words (insert), searching for words (search), and checking if a word starts with a given prefix (starts_with).

# The insert method inserts a word into the Trie by creating nodes for each character in the word.

# The search method checks if a given word exists in the Trie by traversing the Trie from the root and following the character path.

# The starts_with method checks if any word in the Trie starts with a given prefix by following the character path from the root.

class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end_of_word = False  # Indicates if a word ends at this node


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Example usage:
if __name__ == "__main__":
    trie = Trie()
    words = ["apple", "app", "banana", "bat", "ball"]

    for word in words:
        trie.insert(word)

    print("Search for 'app':", trie.search("app"))  # Should return True
    print("Search for 'ap':", trie.search("ap"))    # Should return False
    print("Starts with 'ba':", trie.starts_with("ba"))  # Should return True
    print("Starts with 'banz':", trie.starts_with(
        "banz"))  # Should return False
