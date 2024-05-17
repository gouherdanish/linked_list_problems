class Node:
    def __init__(self,val,next=None) -> None:
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
    def isPalindrome(self, head) -> bool:
        """
        Idea - 
        - Convert the linked list to an array
        - check if array is a palindrome by checking its reverse
        
        Time - O(n)
        Space - O(n)
        """
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        i,j = 0,len(arr)-1
        print(arr)
        print(head)
        while i <= j and arr[i] == arr[j]:
            i += 1
            j -= 1
        if i > j: return True
        return False
    
class Solution:
    def isPalindrome(self, head) -> bool:
        """
        Idea
        - First Pass - Traverse the linked list and push to stack (LIFO)
        - Second Pass - Traverse the linked list again and compare the popped elem with current elem

        Time - O(n)
        Space - O(n)
        """
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        print(stack)
        print(curr)
        print(head)
        curr = head
        while curr and curr.val == stack.pop():
            curr = curr.next
        return curr is None

class Solution2:
    def isPalindrome(self, head) -> bool:
        """
        Idea
        - Create a reversed Linked List
        - Traverse and compare if both are same

        Time - O(n)
        Space - O(n) - Out of place reversal
        """
        # print(head)
        rev = self.reverse(head)
        curr = head
        while curr and curr.val == rev.val:
            # print(curr,rev)
            curr = curr.next
            rev = rev.next
        return curr is None

    def reverse(self,node):
        prev = None
        curr = node
        while curr:
            new = Node(curr.val)
            new.next = prev
            prev = new
            curr = curr.next
        return prev
    
class Solution3:
    """
    Idea
    - Traverse to the middle of the linked list using slow and fast pointers
        - After this slow will point to middle onwards elements in the same order
    - Reverse the slow half of Linked List
        - But prev will point
    """
    def reverse(self,head):
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def isPalindrome(self, head) -> bool:
        # print(head)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #     print(f'{slow} +++ {fast} +++ {head}')
        # print(f'{slow} +++ {fast} +++ {head}')
        rev = self.reverse(slow)
        # print(f'{rev} === {head} == {slow}')
        while rev and rev.val == head.val:
            rev = rev.next
            head = head.next
        return rev is None
        

if __name__=='__main__':
    l = Node(1,Node(2,Node(1)))
    print(l)
    print(Solution3().isPalindrome(l))