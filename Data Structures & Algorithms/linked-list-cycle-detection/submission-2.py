# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        elif head.next is not None and head.next==head :
            return True
        elif head.next is not None:
            a= head.next
            x= head.next.next
            while x is not None and x.next is not None and a is not None:
                if a==x:
                    return True
                a=a.next
                x=x.next.next
        return False