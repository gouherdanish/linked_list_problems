class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        res = ""
        while self.next:
            res += f'{self.val}, '
            self = self.next
        res += f'{self.val}'
        return res

class Solution:
    def length(self,head):
        curr = head
        count = 0
        while curr:
            count+=1
            curr = curr.next
        return count

    def middleNode(self, head):
        if not head or not head.next: 
            return head
        n = self.length(head)
        i = 1
        curr = head
        while i < n // 2 + 1: 
            curr = curr.next
            i += 1
        return curr