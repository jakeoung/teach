import marimo

__generated_with = "0.7.14"
app = marimo.App(width="medium")


app._unparsable_cell(
    r"""
    import heapq
    from collections import defaultdict, Counter

    class Node:
        def __init__(self, freq, symbol, left=None, right=None, level=0):
            self.freq = freq
            self.symbol = symbol
            self.left = left
            self.right = right
            self.huff = ''
            self.level = level

        def __lt__(self, other):
            return self.freq < other.freq

    def build_huffman_tree(frequencies):
        heap = [Node(freq, symbol) for symbol, freq in frequencies.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)

            left.huff = '0'
            right.huff = '1'

            new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right, len(left.symbol + right.symbol))
            heapq.heappush(heap, new_node)

        return heap[0]

    def encode_symbol(tree, symbol):
        
        

    def generate_codes(node, current_code='', codes={}):
        if node is None:
            return

        if node.left is None and node.right is None:
            codes[node.symbol] = current_code

        generate_codes(node.left, current_code + '0', codes)
        generate_codes(node.right, current_code + '1', codes)

        return codes

    def huffman_encoding(probs):
        huffman_tree = build_huffman_tree(probs)
        huffman_codes = generate_codes(huffman_tree)

        encoded_data = ''.join([huffman_codes[symbol] for symbol in data])

        return encoded_data, huffman_tree

    def huffman_decoding(encoded_data, huffman_tree):
        decoded_data = ''
        current_node = huffman_tree

        for bit in encoded_data:
            # print(current_node.level)
            if bit == '0':
                current_node = current_node.left
            else:
                current_node = current_node.right

            if current_node.left is None and current_node.right is None:
                decoded_data += current_node.symbol
                current_node = huffman_tree

        return decoded_data

    #-------------------
    # Data collection
    #-------------------

    data = \"aaab\"
    probs = Counter(data)
    N = sum(probs.values())

    for key in probs.keys():
        probs[key] /= N 

    encoded_data, huffman_tree = huffman_encoding(probs)
    print(f\"Encoded data: {encoded_data}\")

    decoded_data = huffman_decoding(encoded_data, huffman_tree)
    print(f\"Decoded data: {decoded_data}\")
    """,
    name="__"
)


@app.cell
def __(probs):
    probs
    return


@app.cell
def __(encoded_data, huffman_encoding, huffman_tree, probs):
    import math 

    def compute_entropy(probs):
        E = 0.0
        for key in probs.keys():
            E += -probs[key] * math.log2(probs[key])
        return E


    def compute_codelength(encoded_data, huffman_tree, probs):
        codelength = 0

        for symbol in encoded_data:
            node = huffman_tree
            length = 0

            while True:
                length += 1
                if symbol == '0':
                    node = node.left
                else:
                    node = node.right

                if node.left is None and node.right is None:
                    break

            print(node.symbol)
            codelength += length*probs[node.symbol]

        return codelength

    entropy = compute_entropy(probs)
    huffman_encoding()
    codelength = compute_codelength(encoded_data, huffman_tree, probs)
    print(f"Entropy: {entropy}, expected codelength: {codelength}")
    return codelength, compute_codelength, compute_entropy, entropy, math


@app.cell
def __(huffman_tree):
    huffman_tree.symbol
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
