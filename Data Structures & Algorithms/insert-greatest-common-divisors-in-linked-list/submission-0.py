# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def igcd(node):
            if node is None:
                return
            if node.next is None:
                return
            else:
                t=node.next
                gcd = math.gcd(t.val,node.val)
                node.next = ListNode(gcd,t)
                igcd(t)
        igcd(head)
        return head