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
    
    @property
    def length(self):
        curr = self
        count = 0
        while curr:
            count+=1
            curr = curr.next
        return count

class Solution1:
    def reverseKGroup(self, head, k):
        """
        Naive Approach
        - Convert linked list to array
        - Create swapped array as per k 
            - slice the array - k elms each in n/k groups
            - for each slice - reverse the slice if it has k elms else leave it
            - keep in result array
        - Convert this array back into Linked List

        Time - O(n)
        Space - O(n)
        """
        # Convert to Array
        headlist = []
        while head:
            headlist.append(head.val)
            head = head.next
        # Create Swapped Array
        anslist = []
        for i in range(0,len(headlist),k):
            sliced = headlist[i:(i+k)]
            print(sliced,anslist)
            if len(sliced) == k:
                sliced.reverse()
                anslist.extend(sliced)
            else:
                anslist.extend(sliced)
        # Convert back into Linked List
        ans = ListNode(0)
        curr = ans
        for i in range(len(anslist)):
            curr.next = ListNode(anslist[i])
            curr = curr.next
        return ans.next

class Solution:
    def reverseKGroup(self, head, k):
        """
        n - length of input linked list
        n%k - these are last remaining elms should be left as is
        (n - n%k) - elms to be reversed in group of k elms

        Steps:
            - Iterate i from 0 to (n - n%k)
            - Take a sliding window of k elms and reverse these
            - return the new head

        Time - O(n)
        Space - O(1)
        """
        n = head.length
        n_rev = n - n%k
        i = 0
        curr = head
        prev_start = head
        ans = ListNode(0)
        while i < n_rev:
            j = 0
            prev = None
            start = curr
            while j < k:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                j += 1
            if i == 0:
                ans.next = prev
            else:
                prev_start.next = prev
                prev_start = start
            i += k
        start.next = curr
        return ans.next

if __name__=='__main__':
    # l = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,ListNode(7)))))))
    l = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    print(l)
    print(l.length)

    k = 3
    print(Solution().reverseKGroup(l,k))