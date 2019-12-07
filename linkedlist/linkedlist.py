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

    def clone(self):
        node = self.head
        cloned = LinkedList()
        while(node):
            cloned.insert(node.data)
            node = node.next
        return cloned

    def pop(self):
        '''
        Pops the head element
        '''
        tmp = self.head
        nxt = self.head.next
        self.head = nxt
        return tmp.data

    def delete(self):
        '''
        Deletes the Entire List
        '''
        while(self.head):
            tmp = self.head.next
            self.head = None
            self.head = tmp

    def insert_to_sorted_pos(self, data):
        '''
        Inserts a node at it's Sorted position
        This function works if the sorting is in Ascending Order
        For Descending order we need to change the '<' to '>'
        '''
        node = self.head
        if node.data < data:
            nxt = self.head.next
            while(nxt and nxt.data <= data):
                node = node.next
                nxt = nxt.next
            new_node = Node(data)
            new_node.next = nxt
            node.next = new_node
        else:
            self.head = Node(data)
            self.head.next = node


def convertToLinkedList(arr):
    l = LinkedList()
    for i in arr:
        l.insert(i)
    return l
