# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getK(node):
            ct=0
            while node and ct<k:
                node=node.next
                ct+=1
            return node

        th = ListNode(next=head)
        groupP=th
        while 1:
            groupEnd=getK(groupP)
            if not groupEnd:
                break
            groupNext=groupEnd.next
            p,c=groupEnd.next,groupP.next
            while c!=groupNext:
                tmp=c.next
                c.next=p
                p=c
                c=tmp
            tmp=groupP.next
            groupP.next=groupEnd
            groupP=tmp
        return th.next
