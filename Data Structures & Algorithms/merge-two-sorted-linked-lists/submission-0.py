# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        n=ListNode()
        def a(i,j,x):
            if i==None:
                x.next=j
            elif j==None:
                x.next=i
            else:
                if i.val<j.val:
                    x.next=i
                    a(i.next,j,x.next)
                else:
                    x.next=j
                    a(i,j.next,x.next)
        a(list1,list2,n)
        return n.next

        