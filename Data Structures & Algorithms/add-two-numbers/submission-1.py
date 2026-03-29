# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        a1=l1
        a2=l2
        while a1 is not None and a2 is not None:
            a=a1.val+a2.val+c
            print(a)
            if a>=10:
                c=1
            else:
                c=0
            a1.val = a%10
            if a1.next is None and c==0:
                a1.next=a2.next
                break
            elif a1.next is None:
                a1.next=ListNode(c)
                c=0
            elif a2.next is None and c!=0:
                a2.next=ListNode(c)
                c=0
            a1=a1.next
            a2=a2.next
        return l1 