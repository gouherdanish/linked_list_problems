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
    def length(self, head):
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count
    
    def rotateRight(self, head, k: int):
        """
        Approach
        - Take two pointers current and previous elm
        - Loop until you reach last elem
        - Adjust pointers as reqd
        - Repeat until k times

        Edge Cases
        - When list has 1 or less elems 
            - return as is
        - when k > n
            - only loop for k % n times
        """
        n = self.length(head)
        if n <= 1: return head
        k = k % n
        if k == 0: return head

        i = 0
        while i < k:
            curr = head
            prev= None
            while curr.next:
                prev = curr
                curr = curr.next
            prev.next = curr.next
            curr.next = head
            head = curr
            i += 1
        return head
                
if __name__=='__main__':
    l = ListNode(1,ListNode(2,ListNode(3)))
    print(l)
    k = 200
    print(Solution().rotateRight(l,k))