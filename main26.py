class Node:
    def __init__(self, number):
        self.left = None
        self.right = None
        self.number = number


class tree:
    def __init__(self):
        self.head = None

    def __iter__(self):
        return self.inorder(self.head)

    def inorder(self, head):
        if head is None:
            return

        yield head.number

        yield from self.inorder(head.left)
        yield from self.inorder(head.right)


tr = tree()

tr.head = Node(3)

tr.head.left = Node(2)
tr.head.right = Node(4)

for i in tr.__iter__():
    print(i)