from list_node import ListNode

def sum_of_linked_list(mylist):
    sum = 0
    while mylist:
        sum+=mylist.val
        mylist = mylist.next
    return sum

if __name__=='__main__':
    l = [-1,0,1]
    ll = curr = ListNode()
    # print(ll)
    for val in l:
        curr.next = ListNode(val)
        curr = curr.next
    print(ll)
    print(sum_of_linked_list(ll))