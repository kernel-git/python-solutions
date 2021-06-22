import random as rnd


class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root_value=0):
        self.root = Node(value=root_value)

    def _insert_node(self, place, new_node):
        if place.left is None and place.right is None:
            choice = rnd.random()
            if choice >= 0.5:
                place.right = new_node
            else:
                place.left = new_node
            return new_node
        if place.left is None:
            place.left = new_node
            return new_node
        if place.right is None:
            place.right = new_node
            return new_node
        choice = rnd.random()
        if choice >= 0.5:
            return self._insert_node(place.right, new_node)
        else:
            return self._insert_node(place.left, new_node)

    def insert_node(self, new_value):
        new_node = Node(value=new_value)
        return self._insert_node(self.root, new_node)

    def _find_height(self, start, height):
        height = height + 1
        left = self._find_height(start.left, height) if start.left is not None else -1
        right = self._find_height(start.right, height) if start.right is not None else -1
        if left == -1 and right == -1:
            return height
        if left == -1:
            return right
        if right == -1:
            return left
        return right if right > left else left

    def find_height(self):
        return self._find_height(start=self.root, height=0)


if __name__ == '__main__':
    tree = Tree(5)
    tree.insert_node(43)
    tree.insert_node(2)
    tree.insert_node(11)
    tree.insert_node(0)
    tree.insert_node(-5)
    tree.insert_node(9)
    tree.insert_node(24)
    tree.insert_node(12)
    tree.insert_node(32)
    tree.insert_node(4)

    print(f'Height: {tree.find_height()}')
