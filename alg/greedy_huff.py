import marimo

__generated_with = "0.7.14"
app = marimo.App()


@app.cell
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def a():
        b=1

@app.cell
def huffman_coding(input_str):
    # Create a dictionary to store the frequency of each character
    freq_dict = {}

    for char in input_str:
        if char not in freq_dict:
            freq_dict[char] = 0

    for char in input_str:
        freq_dict[char] += 1

    # Convert the dictionary into a list of tuples
    heap = []
    for key, value in freq_dict.items():
        node = Node(key, value)
        heapq.heappush(heap, (node.freq, node))

    while len(heap) > 1:
        freq1, node1 = heapq.heappop(heap)
        freq2, node2 = heapq.heappop(heap)

        merged = Node(None, freq1 + freq2)
        merged.left = node1
        merged.right = node2

        heapq.heappush(heap, (merged.freq, merged))

    # Huffman coding
    huffman_codes = {}

    def generate_code(node, current_code):
        if node.char is not None:
            huffman_codes[node.char] = current_code
            return

        generate_code(node.left, current_code + "0")
        generate_code(node.right, current_code + "1")

    generate_code(heap[0], "")

    return huffman_codes

@app.cell
def __(mo):
    input_str = "this is an example for huffman coding"
    print(huffman_coding(input_str))


if __name__ == "__main__":
    app.run()
return Node, app, heapq, huffman_coding, marimo

