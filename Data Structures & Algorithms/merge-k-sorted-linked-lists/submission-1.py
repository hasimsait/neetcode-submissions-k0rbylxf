# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        if len(lists)==1:
            return lists[0]
        def merge2(i,j):
            if i is None:
                return j
            if j is None:
                return i
            if i.val<=j.val:
                i.next = merge2(i.next,j)
                return i
            j.next = merge2(i,j.next)
            return j
        a=lists[0]
        for i in range(1,len(lists)):
            a=merge2(a,lists[i])
        return a

            