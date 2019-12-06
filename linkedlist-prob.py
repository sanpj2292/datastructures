from linkedlist import LinkedList, convertToLinkedList, Node


def remove_dup_main():
    sorted_ll = convertToLinkedList([1, 1, 1, 2, 4, 4, 6, 9, 9])
    print('Before Duplicates removal: ')
    sorted_ll.printAll()
    remove_dup_sorted_ll(sorted_ll)
    print('After Duplicates removal: ')
    sorted_ll.printAll()


def remove_dup_sorted_ll(l: LinkedList):
    '''
    Remove Duplicate nodes from Sorted LinkedList
    '''
    node = l.head
    nxt = node.next
    while nxt:
        if node.data == nxt.data:
            node.next = nxt.next
        else:
            node = node.next
        nxt = nxt.next


def moveEvenNodeToEnd_Rev(l: LinkedList):
    '''
        Move even nodes to the end of the list in reverse order
        LL: 1->3->5->6->89->2->45->8->34->23->74
        Iteration-1: odd = 1, even = 3
        Iteration-2: odd = 5, even = 6
        Iteration-3: odd = 89, even = 2
        .
        .
        .
        odd Node's next will be the even LinkedList
    '''
    odd = l.head  # Odd Node
    even_ll = LinkedList()  # Another LinkedList
    even = odd.next  # Even Node
    while(odd and odd.next):
        if even:
            tmp = even_ll.head
            new_odd = Node(even.data)
            new_odd.next = tmp
            even_ll.head = new_odd
            odd.next = even.next
        if odd.next:
            odd = odd.next
            even = odd.next
    odd.next = even_ll.head


if __name__ == "__main__":
    # remove_dup_main()
    ll = convertToLinkedList([1, 3, 5, 6, 89, 2, 45, 8, 34, 23, 74])
    ll.printAll()
    moveEvenNodeToEnd_Rev(ll)
    ll.printAll()
