import heapq


class Node:
    def __init__(self, letter, frequency):
        self.parent = None
        self.left = None
        self.right = None
        self.letter = letter
        self.frequency = frequency


def traversal(huffman_tree, path, words):

    if huffman_tree.left is not None:
        path.append('0')
        words = traversal(huffman_tree.left, path, words)
        path.pop()

    if len(huffman_tree.letter) == 1:
        words.append((huffman_tree.letter, ''.join(path)))

    if huffman_tree.right is not None:
        path.append('1')
        words = traversal(huffman_tree.right, path, words)
        path.pop()

    return words


input = open('input.txt', 'r')
output = open('output.txt','w')
characters_list = list(input.read())

count = {}
frequency = {}
h = []
heapq.heapify(h)
total = len(characters_list)
for i in characters_list:
    if i in count:
        count[i] = count[i] + 1
    else:
        count[i] = 1
for key, value in count.items():
    frequency[key] = (value / total)
    heapq.heappush(h, (frequency[key], key, (Node(key, frequency[key]))))
print(h)

while len(h) > 1:

    n = Node(None, 0)
    a = heapq.heappop(h)
    b = heapq.heappop(h)
    n.left = a[2]
    n.right = b[2]
    n.frequency = n.left.frequency + n.right.frequency
    n.letter = n.left.letter + n.right.letter
    heapq.heappush(h, (n.frequency, n.letter, n))
path = []
words = []
huffman_tree = heapq.heappop(h)
traversal(huffman_tree[2], path, words)
words.sort()
print('Znak    Powtórzenia  Kod',file=output)
for pair in words:
    string = "{letter:5s}  ({count:3d})    {code:<10}"
    print(string.format(letter=pair[0], freq=frequency[pair[0]], count=count[pair[0]], code=pair[1]),file=output)

input.close()
