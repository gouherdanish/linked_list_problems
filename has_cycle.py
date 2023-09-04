from list_node import ListNode

def has_cycle(mylist):
    slow = fast = mylist
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

if __name__=='__main__':
    l = [-1,0,1,0]
    ll = curr = ListNode()
    # print(ll)
    for val in l:
        curr.next = ListNode(val)
        curr = curr.next
    print(ll.next)
    print(has_cycle(ll.next))