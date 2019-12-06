class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'{self.data}'


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            self._insert(self.head, data)

    def _insert(self, node, data):
        if node.next:
            node = node.next
            self._insert(node, data)
        else:
            node.next = Node(data)

    def printAll(self):
        node = self.head
        while(node):
            print(node.data, end='->' if node.next else '\n')
            node = node.next


def convertToLinkedList(arr):
    l = LinkedList()
    for i in arr:
        l.insert(i)
    return l
