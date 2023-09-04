from typing import Optional
from list_node import ListNode


def removeNthFromEnd(list1: Optional[ListNode],pos_from_end:int) -> Optional[ListNode]:
    res = ListNode(next=list1)
    curr = prev = res
    while curr.next:
        curr = curr.next
        if pos_from_end==0:
            prev = prev.next
        else:
            pos_from_end-=1
    prev.next = prev.next.next
    return res.next
    

if __name__ == '__main__':
    """
    Algo:
        Create curr and prev pointers with pos_from_end as distance between them
        Iterate until curr reaches the end and then assign prev.next = prev.next.next so as to skip that element
    """
    l1 = [1,3,4,5,7,2]
    pos_from_end = 1
    list1 = curr1 = ListNode()
    for val in l1:
        curr1.next = ListNode(val)
        curr1 = curr1.next
    print(removeNthFromEnd(list1.next,pos_from_end))