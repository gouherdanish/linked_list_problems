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
    
def insert(prev,newval):
    new_node = Node(newval)
    new_node.next = prev.next
    prev.next = new_node

if __name__=='__main__':
    node = Node(1,Node(2,Node(3,Node(4))))
    print(node)
    print(node)

    insert(node.next, 5)
    print(node)
