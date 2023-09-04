from list_node import ListNode
from typing import Optional

def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    """Remove a target element from the given list
    e.g. 
        input list = [3,1,5,2,3] 
        target 3
        
        output list = [1,5,2]

    Logic:
        Start with an empty result list
        Iterate through the input list, 
            if the node's value != target value: append to the result list
    
    Args:
        head (Optional[ListNode]): input list
        val (int): target element to be removed

    Returns:
        Optional[ListNode]: output list
    """    
    res = ListNode()
    worker_res = res
    if head:    
        curr = head
        while curr:
            if curr.val != val:
                worker_res.next = ListNode(val=curr.val)
                worker_res = worker_res.next
            curr = curr.next
    return res.next

if __name__=='__main__':
    l = [3,1,5,2,3]
    target = 3
    ll = curr = ListNode()
    # print(ll)
    for val in l:
        curr.next = ListNode(val)
        curr = curr.next
    print(ll.next)
    print(removeElements(ll.next, target))