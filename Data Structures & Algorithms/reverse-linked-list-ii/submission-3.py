# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left==right:
            return head
        def s(node,inRange,p,c):
            if not node:
                return None
            if not inRange:
                if c !=left:
                    node.next = s(node.next,inRange,node,c+1)
                    return node
                else:
                    t = s(node.next,True,node,c+1)
                    node.next = t[1] if t else None
                    return t[0] if t else node
            if inRange:
                a=node.next
                node.next = p
                if c !=right:
                    return s(a,True,node,c+1)
                else:
                    return [node,a]
        return s(ListNode(-10000,head),False,None,0).next
            
