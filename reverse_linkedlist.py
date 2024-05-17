class ListNode:
    def __init__(self,val=0,next=None) -> None:
        self.val = val
        self.next = next
        
    def __str__(self) -> str:
        curr = self
        res = ''
        while curr.next:
            res += f'{curr.val}, '
            curr = curr.next
        return res + str(curr.val)
    
    def __repr__(self) -> str:
        return str(self)
    
    def reverse(self):
        if self:
            curr_node = self
            prev_node = None
            while curr_node:
                next_node = curr_node.next
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = next_node
            return prev_node
        else:
            return None
        
# class LinkedList:
#     def __init__(self,head) -> None:
#         self.head = head
    
#     def __str__(self) -> str:
#         curr = self.head
#         res = ''
#         while curr.next:
#             res += f'{curr.val}, '
#             curr = curr.next
#         return res + str(curr.val)
    
#     def __repr__(self) -> str:
#         return str(self)
    
#     def reverse(self):
#         if self.head:
#             curr_node = self.head
#             prev_node = None
#             while curr_node:
#                 next_node = curr_node.next
#                 curr_node.next = prev_node
#                 prev_node = curr_node
#                 curr_node = next_node
#             return prev_node
#         else:
#             return None
    
if __name__=='__main__':
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    print(head)
    print(head.reverse())
    # ll = LinkedList(head)
    # print(ll)
    # print(ll.reverse())
    # print(ll)

