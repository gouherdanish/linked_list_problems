from list_node import ListNode

def deleteDuplicates(mylist):
    """
    Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
    leaving only distinct numbers from the original list. 
    Return the linked list sorted as well.
    e.g.
        input list = [1,2,3,3,4,4,5]
        output list = [1,2,5]

    Logic:
        A current element is not a duplicate when
            - its prev node is not same and
            - its next node is not same

    Args:
        mylist (ListNode): sorted linked list

    Returns:
        ListNode: sorted linked list having duplicates deleted completely
    """
    res = ListNode()
    new_node = res

    prev_node = None
    curr_node = mylist
    next_node = curr_node

    iter = 1
    while curr_node:
        next_node = next_node.next
        next_is_not_same = curr_node.val != next_node.val if next_node else True
        prev_is_not_same = curr_node.val != prev_node.val if prev_node else True
        if next_is_not_same and prev_is_not_same:
            new_node.next = ListNode(val=curr_node.val)
            new_node = new_node.next
        prev_node = curr_node
        curr_node = next_node
        iter +=1
    return res.next

if __name__=='__main__':
    l = [1,2,3,3,4,4,5]
    ll = curr = ListNode()
    # print(ll)
    for val in l:
        curr.next = ListNode(val)
        curr = curr.next
    print(ll)
    print(deleteDuplicates(ll.next))