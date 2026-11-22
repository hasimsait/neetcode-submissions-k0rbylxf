# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: Optional[ListNode], a: int, b: int, list2: Optional[ListNode]) -> Optional[ListNode]:
        h=list1
        ct = 1
        while ct<a and h.next:
            h=h.next
            ct+=1
        t=h
        while ct-2<b and t.next:
            t=t.next
            ct+=1
        h.next = list2
        while h.next:
            h=h.next
        h.next = t
        return list1
