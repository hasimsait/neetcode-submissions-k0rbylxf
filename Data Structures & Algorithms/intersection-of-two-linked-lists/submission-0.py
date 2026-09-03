# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ta,tb,la,lb = headA,headB,0,0
        while ta:
            la+=1
            ta=ta.next
        while tb:
            lb+=1
            tb=tb.next
        if la<lb:
            headA,headB = headB,headA
            la,lb=lb,la
        while la>lb:
            headA=headA.next
            la-=1
        while headA and headA!=headB:
            headA=headA.next
            headB=headB.next
        return headA

