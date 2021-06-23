class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __iter__(self):
        return BSTIterator(self)


class BSTIterator:
    def __init__(self, root):
        self.stack = []
        curr = root

        while curr:
            self.stack.append(curr)
            curr = curr.left


    def __next__(self):
        if not self.stack:
            raise StopIteration()

        node = self.stack.pop()
        value = node.value
        node = node.right

        while node:
            self.stack.append(node)
            node = node.left

        return value


    def __iter__(self):
        return self


root = Node(5, Node(3, Node(1), Node(4)), Node(10, (Node(6, None, Node(7)))))

for i in root:
    print(i, end = ' ')

print()

# list(root)
# [1, 3, 4, 5, 6, 7, 10]
