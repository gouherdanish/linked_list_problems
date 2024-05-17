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

class Solution1:
    def swapPairs(self, head):
        """
        Input:
            head -> A -> B -> C -> D -> NULL

            A -> C
            ^
            |
            B
        Output:
            head -> B -> A -> D -> C -> NULL

        curr = head => A
        next = curr.next => B
        curr.next = next.next => A.next = B.next = C
        next.next = curr => B.next = A

        Time - O(n)
        """
        if not head or not head.next: 
            return head
        curr = head
        ans = head.next
        prev = None
        while curr and curr.next:
            print(curr, prev, ans)
            # swap pointers
            next = curr.next
            curr.next = next.next
            next.next = curr
            if prev:
                prev.next = next
            
            # update pointers
            prev = curr
            curr = curr.next
            print("NEXT",curr, prev, next)
        return ans
        
class Solution:
    def swapPairs(self, head):
        """
        Time - O(n)
        """
        ans = ListNode(0)
        ans.next = head
        prev = ans
        curr = head
        while curr and curr.next:
            first = curr
            second = curr.next

            first.next = second.next
            second.next = first
            prev.next = second

            prev = curr
            curr = curr.next
        return ans.next


if __name__=='__main__':
    l = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6))))))
    # l = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    print(l)
    print(Solution().swapPairs(l))