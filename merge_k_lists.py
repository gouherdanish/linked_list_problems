from typing import Optional
from list_node import ListNode


def mergeTwoLists(list1,list2) -> Optional[ListNode]:
    """Merge two sorted linked lists so as to create a sorted linked list

    Args:
        list1 (Optional[ListNode]): sorted list
        list2 (Optional[ListNode]): sorted list

    Returns:
        Optional[ListNode]: merged and sorted list
    """    
    res = ListNode()
    curr = res
    while True:
        print(list1,list2,res)
        # print(res)
        if list1 is None:
            curr.next = list2
            break
        if list2 is None:
            curr.next = list1
            break
        if list1.val < list2.val:
            curr.next = ListNode(val=list1.val)
            list1 = list1.next
        else:
            curr.next = ListNode(val=list2.val)
            list2 = list2.next
        curr = curr.next
        # print(res)
    return res.next

def mergeKLists(lists):
    print("XXX")
    print(len(lists))
    print(lists)
    if len(lists) == 1:
        return lists[0]
    elif len(lists) == 2:
        return mergeTwoLists(lists[0],lists[-1])
    else:
        return mergeTwoLists(mergeKLists(lists[:-1]),lists[-1])


if __name__ == '__main__':
    """
    Algo:
        Iterate and keep comparing the list elements
        Whichever is smaller, add that as ListNode
        Break when either of the list is empty by assigning the other list as ListNode
    """
    l1 = [1,2]
    l2 = [1,3,5,7,8]
    l3 = [4,6]
    l4 = [5,9,10]
    list1 = curr1 = ListNode()
    list2 = curr2 = ListNode()
    list3 = curr3 = ListNode()
    list4 = curr4 = ListNode()
    for val in l1:
        curr1.next = ListNode(val)
        curr1 = curr1.next
    for val in l2:
        curr2.next = ListNode(val)
        curr2 = curr2.next
    for val in l3:
        curr3.next = ListNode(val)
        curr3 = curr3.next
    for val in l4:
        curr4.next = ListNode(val)
        curr4 = curr4.next
    print(mergeKLists([list1.next,list2.next,list3.next,list4.next]))