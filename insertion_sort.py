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

class Solution1:
    def insertionSortList(self,head):
        """
        - Iterate until last elem (pivot) is Null
        - for each pivot elem
            - If pivot < head then Change head : Move pointer until the pivot elem and swap with head
            - Else 
                - First move pointer to find place s.t. prev < pivot < curr
                - Then move pointer until the pivot elem and swap with curr/prev
        
        Time - O(n^2)
        Space - O(1) - Inplace Sort

        Gives TLE
        """
        if not head or not head.next: 
            return head
        last = head.next

        while last:
            prev = head
            curr = head
            pivot = last.val
            if pivot < head.val:
                while curr.next != last:
                    curr = curr.next
                curr.next = last.next
                last.next = head
                head = last
            else:
                while pivot >= curr.val and curr.next != last:
                    prev = curr
                    curr = curr.next
                next = curr
                while next.next != last:
                    next = next.next
                if pivot < curr.val:
                    prev.next = last
                    next.next = last.next
                    last.next = curr
                    last = next.next
                    continue
            last = last.next
        return head

class Solution2:
    def add(self,node):
        curr = self.ans
        prev = curr
        while curr:
            if curr.val < node.val:
                prev = curr
                curr = curr.next
            else:
                break
        node.next = prev.next
        prev.next = node

    def insertionSortList(self,head):
        """
        Approach
        - Create ans list with a dummy node of minimum value (-5001 from constraints)
        - Pluck nodes from original list and add to ans list keeping sorted order

        Time - O(n^2)
        Space - O(n) - Out of place sorting
        """
        self.ans = ListNode(-5001)
        while head:
            temp = head
            head = head.next
            temp.next = None
            self.add(temp)
        return self.ans.next


class Solution:
    def insertionSortList(self,head):
        """
        Approach
        - Create dummy node and point to head
        - Take last_sorted pointer as head and curr pointer as head.next
        - If curr is greater than last_sorted, then move both pointers to next
        - else it means curr should be inserted in the list from (0 to last_sorted)
        
        Time = O(n^2)
        Space - O(1) - In place sort
        """
        ans = ListNode(-5001,head)
        last_sorted = head
        curr = head.next
        while curr:
            if curr.val > last_sorted.val:
                last_sorted = last_sorted.next
                curr = curr.next
            else:
                prev = ans
                while prev.next.val < curr.val:
                    prev = prev.next
                last_sorted.next = curr.next
                curr.next = prev.next
                prev.next = curr
                curr = last_sorted.next
        return ans.next
 
if __name__=='__main__':
    # l = ListNode(4,ListNode(2,ListNode(1,ListNode(3,ListNode(5)))))
    l = ListNode(-1,ListNode(5,ListNode(3,ListNode(4,ListNode(0)))))
    # l = ListNode(1,ListNode(9,ListNode(7,ListNode(4,ListNode(8,ListNode(-1,ListNode(6)))))))
    print(l)
    print(Solution().insertionSortList(l))