# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def s(h,p):
            if h is None:
                return h
            if h.next is None:
                h.next=p
                return h
            else:
                a=s(h.next,h)
                h.next=p
                return a
        return s(head,None)
