from list_node import ListNode

def add_two_linked_lists(mylist1,mylist2):
    """Finds the addition of two numbers using linked list

    Args:
        mylist1 (ListNode): First list having digits of the first number in reverse order
        mylist2 (ListNode): Second list having digits of the first number in reverse order

    Returns:
        ListNode: Output list containing the digits of the sum in reverse order
    """    
    sum = 0
    keep,carry = 0,0
    res = ListNode()
    curr = res

    curr1 = mylist1
    curr2 = mylist2
    while curr1 or curr2:
        print("START")
        print(curr1)
        print(curr2)
        if curr2 is None:
            print("1")
            sum = curr1.val + carry
            curr1 = curr1.next
        elif curr1 is None:
            print("2")
            sum = curr2.val + carry
            curr2 = curr2.next
        else:
            print("3")
            sum = curr1.val + curr2.val + carry
            curr1 = curr1.next
            curr2 = curr2.next
        keep,carry = sum%10, sum//10
        curr.next = ListNode(keep)
        curr = curr.next
        print(sum,carry,keep,res)
        print("END")
    return res.next


def add_two_linked_lists(mylist1,mylist2):
    """Finds the addition of two numbers using linked list

    Args:
        mylist1 (ListNode): First list having digits of the first number in reverse order
        mylist2 (ListNode): Second list having digits of the first number in reverse order

    Returns:
        ListNode: Output list containing the digits of the sum in reverse order
    """    
    keep,carry = 0,0
    res = ListNode()
    curr = res

    while mylist1 or mylist2:
        result = carry
        if mylist1:
            result += mylist1.val
            mylist1 = mylist1.next
        if mylist2:
            result += mylist2.val
            mylist2 = mylist2.next
        keep,carry = result%10, result//10
        curr.next = ListNode(keep)
        curr = curr.next
        if mylist1 is None and mylist2 is None and carry > 0:
            curr.next = ListNode(carry)
            curr = curr.next
    return res.next


if __name__=='__main__':
    """
    Algo:
        Iterate and sum the elements of the two list one by one
        Use keep and carry for unit and tens digit of the sum
        Create ListNode with Keep digit and pass on carry to next iteration
        If both list are exhausted and carry is left, create a ListNode with carry digit.
    """
    l1 = [9,9]
    l2 = [9,9,9]
    list1 = curr1 = ListNode()
    list2 = curr2 = ListNode()
    for val in l1:
        curr1.next = ListNode(val)
        curr1 = curr1.next
    for val in l2:
        curr2.next = ListNode(val)
        curr2 = curr2.next
    print(add_two_linked_lists(list1.next,list2.next))