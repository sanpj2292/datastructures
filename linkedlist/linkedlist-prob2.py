from linkedlist import LinkedList, convertToLinkedList, Node

'''
1) Find K’th node from the end in a linked list
2) Merge alternate nodes of two linked lists into the first list
'''


def mergeAlternateNodes(l1: LinkedList, l2: LinkedList):
    '''
        Merge Alternate nodes of two linked lists into the first list
        l1 = {1,2,3}
        l2 = {4,5,6,7,8}

        Result:
        l1 = {1,4,2,5,3,6}
        l2 = {7,8}
    '''
    n1 = l1.head
    n2 = l2.head
    while(n1 and n2):
        # if i % 2 != 0:
        tmp = n2.next
        new_node = Node(n2.data)
        new_node.next = n1.next
        n1.next = new_node
        n2 = tmp
        n1 = n1.next.next
    # Change the head to the last Node that is present after above Iteration
    l2.head = n2
    l1.printAll()
    l2.printAll()


def findKthNodeFromEnd(l: LinkedList, k: int):
    '''
        Find Kth node from the end in a LinkedList
    '''
    node = l.head
    if k <= 0:
        print('The value of k should be > 0')
        return
    if not node:
        print('Cannot Find requested Element from Empty LinkedList')
        return
    memo = {}
    ind = 1
    if node.next:
        while(node):
            memo[ind] = node.data
            if node.next:
                ind += 1
            node = node.next
        if k > ind:
            print('No Element exists, since k exceeds length of LinkedList')
            return
        else:
            return memo.get(ind - k + 1)
    else:
        if k > 1:
            print('Only one node exists in LinkedList & k > 1')
            return
        else:
            return node.data


def moveLastNodeToFront(l: LinkedList):
    node = l.head
    if not node.next:
        print('Cannot move the last node since the last node is first node')
    else:
        while(node.next.next):
            node = node.next
        # node will be the last-but one Node
        lastNode = node.next
        node.next = None
        firstNode = l.head
        lastNode.next = firstNode
        l.head = lastNode
        l.printAll()


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
    # ll = convertToLinkedList([1, 2, 3, 4, 5])
    # ll = convertToLinkedList([1, 8, 3, 2, 4, 6, 7, 5, 9])
    # ll = convertToLinkedList([1])
    # d = split_mid(ll)
    # print(d)
    # d = split_into_two_lists(ll)
    # print('First List')
    # d[0].printAll()
    # print('Second List')
    # d[1].printAll()
    # moveLastNodeToFront(ll)
    # kth = findKthNodeFromEnd(ll, 5)
    # print(kth)
    l1 = convertToLinkedList(list(range(1, 4, 1)))
    l2 = convertToLinkedList(list(range(4, 9, 1)))
    mergeAlternateNodes(l1, l2)
