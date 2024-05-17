class Node:
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
    
def reverse(head):
    """
    Iterative

    Input:
        head -> 1 -> 2 -> 3 -> Null

    Output:
        head -> 3 -> 2 -> 1 -> Null

    Approach
    - keep a current, previous and next pointer
    - Iterate until the end of linked list and shift pointers
    """
    curr = head
    prev = None
    while curr:
        # reverse the current pointer
        next = curr.next
        curr.next = prev
        
        # update pointers
        prev = curr
        curr = next
    return prev

def reverse_rec(head):
    # if not head.next:
    # curr = head
    # node.ne
    pass

if __name__=='__main__':
    node = Node(1,Node(2,Node(3,Node(4))))
    print(node)

    node = reverse(node)
    print(node)