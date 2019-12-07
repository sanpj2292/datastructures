from linkedlist import LinkedList, convertToLinkedList, Node


def split_into_two_lists(l: LinkedList):
    '''
    Split given linked list into two lists where each list 
    containing alternating elements from it

    '''
    i = 0
    node = l.head
    list1 = LinkedList()
    list2 = LinkedList()
    h1 = list1.head
    h2 = list2.head
    while(node):
        new_node = Node(node.data)
        if i % 2 == 0:
            if h1:
                h1.next = new_node
            else:
                list1.head = new_node
                h1 = list1.head
            if h1.next:
                h1 = h1.next
        else:
            if h2:
                h2.next = new_node
            else:
                list2.head = new_node
                h2 = list2.head
            if h2.next:
                h2 = h2.next
        node = node.next
        i += 1
    return list1, list2


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
    # d = split_mid(ll)
    # print(d)
    d = split_into_two_lists(ll)
    print('First List')
    d[0].printAll()
    print('Second List')
    d[1].printAll()
