# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a=set()
        x= head
        while x is not None:
            if x in a:
                return True
            a.add(x)
            x=x.next
        return False