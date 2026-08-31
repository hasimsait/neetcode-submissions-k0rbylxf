# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right==left:
            return head
        ct=1
        t=head
        r=ListNode(0,head)
        prev= r
        first = None
        he = None
        while t and ct<right:
            if ct==left:
                first=t
                he = prev
                prev=t
                t=t.next
            elif ct>left:
                c=t.next
                t.next=prev
                prev=t
                t=c
            else:
                prev=t
                t=t.next
            ct+=1
        if ct==right:
            c=t.next
            t.next=prev
            if first:
                first.next = c
            if he:
                he.next = t
        return r.next
