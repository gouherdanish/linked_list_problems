class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        res = ''
        curr = self
        while curr.next:
            res += f'{curr.val}, '
            curr = curr.next
        res += f'{curr.val}'
        return res
    
    def __repr__(self) -> str:
        return str(self)

class Solution:
    def removeNthFromEnd(self, head, n: int):
        new_head = ListNode(val=0,next=head)
        # prev = new_head
        # curr = new_head
        prev = head
        curr = head
        while curr.next:
            curr = curr.next
            if n == 0:
                prev = prev.next
            else:
                n-=1
            print(f'n : {n} => {prev} ==== {curr} ==== {new_head} == {head}')
        prev.next = prev.next.next
        print(f'n : {n} => {prev} ==== {curr} ==== {new_head} == {head} == {new_head.next}')
        return new_head.next

  
if __name__=='__main__':
    lst = ListNode(1,
                   ListNode(2,
                            ListNode(5,
                                     ListNode(3,
                                              ListNode(4)))))
    print(Solution().removeNthFromEnd(lst,2))
    print(lst)