import heapq

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ""

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(chars, freqs):
    nodes = [Node(freq, char) for char, freq in zip(chars, freqs)]
    heapq.heapify(nodes)

    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, new_node)

    return nodes[0]

def print_huffman_codes(node, val=""):
    if node is not None:
        if node.symbol is not None:
            print(f"{node.symbol} -> {val}")
        print_huffman_codes(node.left, val + "0")
        print_huffman_codes(node.right, val + "1")

# Accept custom input
n = int(input("Enter the number of characters: "))
chars = []
freqs = []

for i in range(n):
    char = input(f"Enter character {i + 1}: ")
    freq = int(input(f"Enter frequency for {char}: "))
    chars.append(char)
    freqs.append(freq)

huffman_tree = build_huffman_tree(chars, freqs)

print("Huffman Codes:")
print_huffman_codes(huffman_tree)





'''This Python code implements the Huffman coding algorithm for data compression. 
It defines a Node class to represent characters with their frequencies and a binary 
tree structure. The build_huffman_tree function constructs the Huffman tree by 
merging nodes with the lowest frequencies iteratively. The print_huffman_codes 
function generates and prints Huffman codes for each character. It accepts user 
input for character frequencies, then builds and displays the Huffman codes. 
The code demonstrates how to create efficient variable-length codes for characters 
based on their frequencies, enabling data compression and decompression. 
It is a fundamental algorithm used in various applications, including file compression 
and data transmission.'''








'''Huffman coding is a method for compressing data efficiently. It assigns 
variable-length binary codes to characters in a way that minimizes the overall
data size. More frequently occurring characters are assigned shorter codes,
while less frequent characters get longer codes. This results in 
significant data compression, where the most common characters are represented 
with fewer bits. When decoding, the codes are read sequentially to reconstruct 
the original data. Huffman coding is widely used in data compression, such as in 
file compression formats (e.g., ZIP) and in data transmission protocols 
(e.g., JPEG for images, MP3 for audio), reducing file sizes while preserving data 
integrity.'''