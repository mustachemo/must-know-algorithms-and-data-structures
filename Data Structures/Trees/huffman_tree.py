# A Huffman tree is a binary tree used for data compression.
# It is constructed based on the frequency of characters in a
# given text or data. Here's a basic implementation of a Huffman tree in Python:

# HuffmanNode represents a node in the Huffman tree. Each node has a character (char), a frequency (frequency), and left and right children.

# build_huffman_tree constructs the Huffman tree based on the frequency of characters in the input text.

# encode_huffman_tree recursively traverses the Huffman tree to build a dictionary that maps characters to their Huffman codes.

# huffman_encoding and huffman_decoding are utility functions for encoding and decoding text using the Huffman tree.

import heapq
from collections import defaultdict, Counter


class HuffmanNode:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency


def build_huffman_tree(text):
    # Count the frequency of each character in the text
    char_frequency = Counter(text)

    # Create a priority queue (min-heap) of HuffmanNodes
    priority_queue = [HuffmanNode(char, freq)
                      for char, freq in char_frequency.items()]
    heapq.heapify(priority_queue)

    # Build the Huffman tree by repeatedly combining the two lowest frequency nodes
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        parent = HuffmanNode(None, left.frequency + right.frequency)
        parent.left = left
        parent.right = right
        heapq.heappush(priority_queue, parent)

    # The root of the heap is the root of the Huffman tree
    return priority_queue[0]


def encode_huffman_tree(node, current_code="", huffman_dict=None):
    if huffman_dict is None:
        huffman_dict = {}

    if node is None:
        return huffman_dict

    if node.char is not None:
        huffman_dict[node.char] = current_code
        return huffman_dict

    huffman_dict = encode_huffman_tree(
        node.left, current_code + "0", huffman_dict)
    huffman_dict = encode_huffman_tree(
        node.right, current_code + "1", huffman_dict)

    return huffman_dict


def huffman_encoding(text):
    if not text:
        return "", None

    root = build_huffman_tree(text)
    huffman_dict = encode_huffman_tree(root)
    encoded_text = "".join([huffman_dict[char] for char in text])

    return encoded_text, root


def huffman_decoding(encoded_text, root):
    if not encoded_text or root is None:
        return ""

    decoded_text = ""
    current_node = root

    for bit in encoded_text:
        if bit == "0":
            current_node = current_node.left
        elif bit == "1":
            current_node = current_node.right

        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = root

    return decoded_text


# Example usage:
if __name__ == "__main__":
    text = "this is an example for huffman encoding"

    encoded_text, huffman_tree = huffman_encoding(text)
    decoded_text = huffman_decoding(encoded_text, huffman_tree)

    print("Original text:", text)
    print("Encoded text:", encoded_text)
    print("Decoded text:", decoded_text)
