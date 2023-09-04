from list_node import ListNode
def reverse(head):
    prev = None
    curr = head
    while curr:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    return prev

def add(l1,l2):
    result = 0
    res = ListNode()
    curr = res
    while l1 or l2:
        if l1:
            result += l1.val
            l1 = l1.next
        if l2:
            result += l2.val
            l2 = l2.next
        keep, carry = result%10, result//10
        curr.next = ListNode(val=keep)
        curr = curr.next
        result = carry
        if not l1 and not l2 and carry > 0:
            curr.next = ListNode(val=carry)
            curr = curr.next
    return res.next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    l1_rev = reverse(l1)
    l2_rev = reverse(l2)
    print(l1_rev)
    print(l2_rev)
    added = add(l1_rev,l2_rev)
    added_rev = reverse(added)
    return added_rev