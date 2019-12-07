from linkedlist import LinkedList, convertToLinkedList, Node


def split_mid(l: LinkedList):
    node = l.head
    if not node:
        return {'Error': 'Empty LinkedList can\'t be split'}
    nxt = node.next
    if nxt:
        i = 1
        midInd = 0
        front_half = []
        back_half = []
        while(nxt):
            if(i % 2 == 0):
                front_half.append(node.data)
                node = node.next
                midInd += 1
            nxt = nxt.next
            i += 1
        if midInd % 2 != 0:
            # Even Lengthed Linkedlist
            front_half.append(node.data)
        node = node.next
        while(node):
            back_half.append(node.data)
            node = node.next
        return {'front': front_half, 'back': back_half}
    else:
        return {'Error': 'Can\'t be split to Front and Back'}


if __name__ == "__main__":
    ll = convertToLinkedList([1, 2, 3, 4, 5])
    d = split_mid(ll)
    print(d)
