# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s=head
        f=head
        while f and f.next:
            s=s.next
            f=f.next.next
        #s is the middle of the linked list
        c,p=s,None
        while c:
            t=c.next
            c.next=p
            p=c
            c=t

        while p and head:
            if p.val!=head.val:
                return False
            head=head.next
            p=p.next
        return True