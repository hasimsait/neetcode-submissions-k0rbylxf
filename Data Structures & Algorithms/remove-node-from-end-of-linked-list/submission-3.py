# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        t,c=head,0
        while t:
            t=t.next
            c+=1
        if c==n:
            return head.next
        t=head
        while c-n>1:
            c-=1
            t=t.next
        t.next=t.next.next if t.next else None
        return head