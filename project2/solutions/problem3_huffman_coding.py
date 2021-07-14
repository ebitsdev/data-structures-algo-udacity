import sys, heapq, collections, operator

class Node:

    def __init__(self, c, frq):
        self.c = c
        self.frq = frq
        self.right = None
        self.left = None

    # Override built-in __lt__ function for ordering
    def __lt__(self, o):
        return o.frq > self.frq

# Sort dictionary values ascending
def frequencies(t_str):
    orderded_col = dict(collections.Counter(t_str))
    sorted_c = collections.OrderedDict(
        sorted(
            orderded_col.items(),
            key=operator.itemgetter(1),
            reverse=False))
    return sorted_c

# Merge nodes together
def generate_nodes():

    while len(h_node) > 1:
        node1 = heapq.heappop(h_node)
        node2 = heapq.heappop(h_node)
        merged_node = Node(None, node1.frq + node2.frq)
        merged_node.left = node1
        merged_node.right = node2
        heapq.heappush(h_node, merged_node)

def h_encode_txt(text):

    encoded_text = ""

    # Ensure the character is a single one
    if len(codes) == 1:
        for c in codes:            
            codes[c] = "0"

    for c in text:
        encoded_text += codes[c]

    return encoded_text

# Utility function to help generate the codes
def utility(n_node, c_code):
    if n_node is None:
        return

    if n_node.c is not None:
        codes[n_node.c] = c_code
        return
    utility(n_node.left, c_code + "0")
    utility(n_node.right, c_code + "1")

def generate_h_node(f_dict):
    for k in f_dict:
        h_node1 = Node(k, f_dict[k])
        h_node.append(h_node1)

def huffman_encoding(data):
    frq_dict = frequencies(data)
    generate_h_node(frq_dict)
    generate_nodes()

    n_tree = heapq.heappop(h_node)
    c_code = ""
    utility(n_tree, c_code)
    h_text = h_encode_txt(data)

    return h_text

def huffman_decoding(c_txt):

    if not c_txt:
        return ""

    c_code = ""
    d_txt = ""

    for bit in c_txt:
        c_code += bit
        if c_code in codes.values():
            for k in codes:
                if c_code == codes[k]:
                    d_txt += k
                    c_code = ""
    return d_txt

# Testing utility function

def test_cases(txt_to_test):

    if txt_to_test:

        print("=====================================")
        print("The size of the data is: {}\n".format(
            sys.getsizeof(txt_to_test)))
        print("The content of the data is: {}\n".format(txt_to_test))

        encoded_data = huffman_encoding(txt_to_test)

        print("The size of the encoded data is: {}\n".format(
            sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data))
        decoded_data = huffman_decoding(encoded_data)

        print("The size of the decoded data is: {}\n".format(
            sys.getsizeof(decoded_data)))
        print("The content of the encoded data is: {}\n".format(decoded_data))
        print("=====================================")
    
    # Handle cases where the string is empty
    else:
        print("There is no string to encode or decode")
    print("_________________________________________")


if __name__ == "__main__":
    codes = {}
    h_node = []
    # Test case with some string
    test_cases("jjjj")
    codes = {}
    h_node = []
    # Test case with normal string
    test_cases("The bird is the word")
    codes = {}
    h_node = []
    # Conduct a test on empty string
    test_cases("")