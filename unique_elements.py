from list_node import ListNode

def getUniqueElements(mylist):
    """
    Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
    leaving only distinct numbers from the original list. Return the linked list sorted as well.
    e.g.
        input list = [1,2,3,3,4,4,5]
        output list = [1,2,3,4,5]
    
    Logic:
        A current node of provided list should be added only 
        when its val is not equal to the current val of resultant linked list

    Args:
        mylist (ListNode): sorted linked list

    Returns:
        ListNode: sorted linked list having only unique elements
    """
    res = ListNode(val=None)
    curr = res
    while mylist:
        # print(mylist)
        if mylist.val != curr.val:
            curr.next = ListNode(val=mylist.val)
            curr = curr.next
        mylist = mylist.next
        # print(res)
    return res.next

if __name__=='__main__':
    l = [-1,-1,0,0,1,1,2,8,8]
    ll = curr = ListNode()
    # print(ll)
    for val in l:
        curr.next = ListNode(val)
        curr = curr.next
    # print(ll)
    print(getUniqueElements(ll.next))