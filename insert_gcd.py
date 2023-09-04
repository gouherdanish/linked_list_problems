from list_node import ListNode

def gcd(a,b):
    return gcd(b,a%b) if b!=0 else a

def insertGreatestCommonDivisors(head):
    ptr1 = head
    ptr2 = head.next
    while ptr2:
        gcd_node = ListNode(val=gcd(ptr1.val,ptr2.val),next=ptr2)
        ptr1.next = gcd_node
        ptr1 = ptr2
        ptr2 = ptr2.next
    return head

if __name__=='__main__':
    l = [1,5,2]
    ll = curr = ListNode()
    # print(ll)
    for val in l:
        curr.next = ListNode(val)
        curr = curr.next
    print(ll.next)
    print(insertGreatestCommonDivisors(ll.next))