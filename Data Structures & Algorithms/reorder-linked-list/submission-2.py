# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def d(node):
            if not node:
                return []
            r= d(node.next)
            r.append(node)
            return r
        elemsrev=d(head)
        elemsrev= elemsrev[:(len(elemsrev)+1)//2]
        t=ListNode(0,head)
        tail=head
        turn = False
        if not head:
            return
        head=head.next
        while len(elemsrev)>0:
            if turn:
                tail.next=head
                head=head.next
            else:
                tail.next=elemsrev.pop(0)
            tail=tail.next
            turn= not turn
        tail.next=None