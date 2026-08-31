# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, list1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        t=None
        l1=list1
        while l1 or l2 or carry:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            s = v1+v2+carry
            print(s)
            carry=s//10
            if l1:
                l1.val=s%10
                if not l1.next:
                    t=l1
            else:
                t.next=ListNode(s%10)
                t=t.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return list1
