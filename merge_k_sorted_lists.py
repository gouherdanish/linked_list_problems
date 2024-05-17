class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val=val
        self.next=next

    def __str__(self):
        res = ''
        curr = self
        while curr.next:
            res = res + f'Node({curr.val}) -> '
            curr = curr.next
        res = res + f'Node({curr.val})'
        return res

    
    def __repr__(self) -> str:
        return str(self)

class Solution:
    def mergeKLists(lists):
        freq_map = {}
        for l in lists:
            curr = l
            while curr:
                freq_map[curr.val] = freq_map.get(curr.val,0) + 1
                curr = curr.next
        freq_map = dict(sorted(freq_map.items()))
        res = ListNode()
        ans = res
        for elm,freq in freq_map.items():
            for _ in range(freq):
                ans.next = ListNode(elm)
                ans = ans.next
        return res.next

        


if __name__=='__main__':
    lists = [
        ListNode(1,ListNode(4,ListNode(5))),
        ListNode(1,ListNode(3,ListNode(4))),
        ListNode(2,ListNode(6))
    ]

    print(lists)
    print(Solution.mergeKLists(lists))

