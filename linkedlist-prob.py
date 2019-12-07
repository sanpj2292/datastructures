from linkedlist import LinkedList, convertToLinkedList, Node


def clone_PalindromeCheck_Fns_Main():
    # Palindrome check function
    ll = convertToLinkedList([1, 3, 2, 3, 1])
    ll = convertToLinkedList([1, 3, 2, 5, 1])
    ll = convertToLinkedList(['R', 'A', 'D', 'A', 'R'])
    ll.printAll()
    print(checkPalindrome(ll))
    # Clone Function Main
    ll1 = ll.clone()
    ll1.head.next.data = 'B'
    print(f'll1: {ll1.head.next.data}')
    print(f'll: {ll.head.next.data}')
    # Pop Function
    print(ll.pop())
    # Delete Function
    ll.delete()
    ll.printAll()


def insertIntoSortPos_main():
    a = [1, 1, 2, 5, 5, 5, 7, 9, 9]
    ll = convertToLinkedList(a)
    ll.printAll()
    ll.insert_to_sorted_pos(8)
    ll.insert_to_sorted_pos(4)
    ll.insert_to_sorted_pos(12)
    ll.insert_to_sorted_pos(1.8)
    ll.printAll()


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


def moveEvenNodeProb_main():
    ll = convertToLinkedList([1, 3, 5, 6, 89, 2, 45, 8, 34, 23, 74])
    ll.printAll()
    moveEvenNodeToEnd_Rev(ll)
    ll.printAll()


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


def checkPalindrome(l: LinkedList):
    '''
        Check if a LinkedList is a Palindrome
        Here we would use 2-pointer approach with Stack
        First we will traverse till mid-point to know if the length of the LL is Odd or Even
        For Example: 
            ll =  1->3->2->3->1
            MidNode is 2
            Stack would not have 2,
            now we would have to Iterate the 2nd half of LinkedList to knw if it indeed is 
            Palindromic LinkedList

        If midpoint is odd,
            node = node.next
        Otherwise
            node is same as midNode
    '''
    node = l.head
    if not node or not node.next:
        return True
    nxt = node.next
    midInd = 0
    i = 1
    stack = []
    while(nxt):
        if i % 2 == 0:
            stack.append(node.data)
            node = node.next
            midInd += 1
        nxt = nxt.next
        i += 1
    if midInd % 2 == 0:
        node = node.next
    while(node):
        if stack.pop(-1) != node.data:
            break
        node = node.next
    return len(stack) == 0


if __name__ == "__main__":
    # remove_dup_main()
    pass
