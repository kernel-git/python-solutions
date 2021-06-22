import random


class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def print_list(head):
    current = head
    while current is not None:
        print(current.value, end=" ")
        current = current.next


def delete_duplicates(head):
    current = head
    while current.next is not None:
        if current.next.value == current.value:
            current.next = current.next.next
            continue
        current = current.next
    return head

head = Node()
prev = head
for i in range(15):
    value = random.randint(prev.value, 10)
    current = Node(value)
    prev.next = current
    prev = current

print_list(head)

print()
delete_duplicates(head)

print_list(head)