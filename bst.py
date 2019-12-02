class Node:
    def __init__(self, data=None):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def __str__(self):
        disp = None
        if self:
            disp = f'''
            {self.data}
            |___ LeftChild: {self.leftChild.data if self.leftChild else None}
            |___ RightChild: {self.rightChild.data if self.rightChild else None}
            '''
        return disp

    def isLeaf(self):
        return (self.leftChild is None and self.rightChild is None)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insert_helper(self.root, data)

    def insert_helper(self, node: Node, data):
        if node.data < data:
            # Go to Right Child
            if node.rightChild:
                self.insert_helper(node.rightChild, data)
            else:
                node.rightChild = Node(data)
        else:
            # Go to Left Child
            if node.leftChild:
                self.insert_helper(node.leftChild, data)
            else:
                node.leftChild = Node(data)

    def traverse(self):
        data_list = []
        self.inOrderTraversal(self.root, data_list)
        return data_list

    def inOrderTraversal(self, node: Node, retArr: list):
        if node.leftChild:
            self.inOrderTraversal(node.leftChild, retArr)
        retArr.append(node.data)
        if node.rightChild:
            self.inOrderTraversal(node.rightChild, retArr)

    def get_predecessor(self):
        pred_node = self.getPredecessor(self.root.leftChild)
        return pred_node.data

    def getPredecessor(self, node: Node):
        if node.rightChild:
            # To return actual value
            return self.getPredecessor(node.rightChild)
        else:
            # Base Condition return to stop Recursion
            return node

    def is_leaf(self, node: Node):
        return (not node.rightChild and not node.leftChild)

    def delete(self, data):
        self.delete_helper(self.root, data)

    def delete_helper(self, node: Node, data):
        if node.data == data:
            if self.is_leaf(node):
                return None
            elif node.leftChild and not node.rightChild:
                return node.leftChild
            elif not node.leftChild and node.rightChild:
                return node.rightChild
            else:
                pred_node = self.getPredecessor(node.leftChild)
                tmp = pred_node.data
                self.delete_helper(node, pred_node.data)
                node.data = tmp
        else:
            if node.data < data:
                node.rightChild = self.delete_helper(node.rightChild, data)
            else:
                node.leftChild = self.delete_helper(node.leftChild, data)
        return node

    def search(self, data):
        node = self.search_helper(self.root, data)
        return node.data

    def search_helper(self, node: Node, data):
        if node.data == data:
            print('Data Found')
            print(node)
            return node
        elif node.data > data:
            return self.search_helper(node.leftChild, data)
        elif node.data < data:
            return self.search_helper(node.rightChild, data)

    def getNodeLevel(self, data):
        level = 0
        node = self.root
        while(node.data != data):
            if data > node.data:
                node = node.rightChild
            elif data < node.data:
                node = node.leftChild
            level += 1
        return level

    def _getAncestorNodesDataList(self, data):
        ancestorNodeDataList = []
        node = self.root
        while(node and node.data != data):
            tmp = node
            if node.data < data:
                node = node.rightChild
            elif node.data > data:
                node = node.leftChild
            ancestorNodeDataList.append(tmp.data)
        return ancestorNodeDataList

    def getLeastCommonAncestor(self, data1, data2):
        if ((self.root.data >= data1 and self.root.data <= data2) or
                (self.root.data <= data1 and self.root.data >= data2)):
            return self.root.data
        else:
            if data1 == data2:
                return data1
            l1 = self.getNodeLevel(data1)
            l2 = self.getNodeLevel(data2)
            if l1 <= l2:
                data = data2
                otherdata = data1
                l = l2
            else:
                data = data1
                otherdata = data2
                l = l1
            ancestorList = self._getAncestorNodesDataList(data)
            if ancestorList[l-1] == otherdata:
                return otherdata
            return ancestorList[l-1]

    def rotateRight(self, data):
        node = self.root
        self.rightRotate(node, data)

    def rightRotate(self, node: Node, data):
        if node:
            if node.data == data:
                # Rotate this Node to the right
                try:
                    if node.leftChild is None:
                        raise ValueError(
                            'Node\'s Left Node is a Leaf Node hence cannot be rotated')
                except ValueError as e:
                    print(e)
                else:
                    new_node = Node(node.data)
                    new_node.rightChild = node.rightChild
                    new_node.leftChild = node.leftChild.rightChild

                    node.data = node.leftChild.data
                    node.leftChild = node.leftChild.leftChild
                    node.rightChild = new_node
            else:
                new_node = node.leftChild if data < node.data else node.rightChild
                self.rightRotate(new_node, data)

    def bfs_iterative(self):
        '''
        Breadth First Search Iterative Function
        '''
        queue = []
        retElements = []
        node = self.root
        queue.append(node)
        while(queue):
            node = queue.pop(0)
            retElements.append(node.data)
            if node.leftChild or not node.isLeaf():
                queue.append(node.leftChild)
            if node.rightChild or not node.isLeaf():
                queue.append(node.rightChild)
        return retElements

    def rotateLeft(self, data):
        self.leftRotate(self.root, data)

    def leftRotate(self, node: Node, data):
        if node:
            if node.data == data:
                try:
                    if node.rightChild is None:
                        raise ValueError(
                            'Node\'s Right Child is None hence cannot be rotated')
                except ValueError as e:
                    print(e)
                else:
                    new_node = Node(node.data)
                    new_node.rightChild = node.rightChild.leftChild
                    new_node.leftChild = node.leftChild

                    node.data = node.rightChild.data
                    node.rightChild = node.rightChild.rightChild
                    node.leftChild = new_node
            else:
                node = node.leftChild if data < node.data else node.rightChild
                self.leftRotate(node, data)


if __name__ == "__main__":
    # tree = BST()
    # tree.insert(5)
    # tree.insert(3)
    # tree.insert(4)
    # tree.insert(2)
    # tree.insert(7)
    # tree.insert(6)
    # tree.insert(8)
    # tree.insert(3.5)
    # tree.insert(3.25)

    # # print(tree.traverse())
    # print(tree.get_predecessor())

    # # tree.delete(7)
    # # print(tree.traverse())
    # print(tree.search(3.5))
    # New Tree
    tree = BST()
    elements = [15, 10, 25, 8, 12, 20, 30, 6, 9, 18, 22]
    for i in elements:
        tree.insert(i)
    # print(tree._getAncestorNodesDataList(6))
    # print(tree.getNodeLevel(12))
    # print(tree.getLeastCommonAncestor(6, 12))
    # print(tree.getLeastCommonAncestor(10, 12))
    # print(tree.getLeastCommonAncestor(20, 6))
    # print(tree.getLeastCommonAncestor(18, 22))
    # print(tree.getLeastCommonAncestor(30, 30))
    # tree.rotateRight(10)
    tree.rotateLeft(15)
    print(tree.bfs_iterative())
    # print(tree.traverse())
