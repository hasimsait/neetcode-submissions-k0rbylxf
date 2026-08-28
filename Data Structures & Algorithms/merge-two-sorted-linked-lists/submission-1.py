# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def s(n1,n2,prev):
            if n1 is None:
                prev.next = n2
            elif n2 is None:
                prev.next = n1
            elif n1.val <= n2.val:
                prev.next = n1
                s(n1.next,n2,n1)
            else:
                prev.next = n2
                s(n1,n2.next,n2)
        t=ListNode()
        s(list1,list2,t)
        return t.next