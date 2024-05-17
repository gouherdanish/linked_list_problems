class ListNode:
    def __init__(self,val=0,next=None) -> None:
        self.val = val
        self.next = next

    # def __str__(self) -> str:
    #     res = ''
    #     curr = self
    #     while curr:
    #         res += f'ListNode({curr.val})'
    #         if curr.next:
    #             res += '->'
    #         curr = curr.next
    #     return f'{res}->None'
        
    def __str__(self) -> str:
        return '->'.join([str(node.val) for node in self])
    
    def __repr__(self) -> str:
        return str(self)

    def __iter__(self):
        curr = self
        while curr:
            yield curr
            curr = curr.next