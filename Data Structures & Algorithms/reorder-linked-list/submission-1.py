# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None:
            return
        mem = {}
        def nextElemsReversed(x):
            if x is None:
                mem[x] = []
                return None
            elif x.next is None:
                mem[x] = [x]
                return [x]
            else:
                mem[x] = nextElemsReversed(x.next)+[x] #8 6 4
                return mem[x]
        nextElemsReversed(head)
        x=head
        for key in mem:
            g=""
            for elem in mem[key]:
                g+=str(elem.val)
            print(key.val,g)
        i=0
        while x is not None:
            t=x.next
            if len(mem[x])>=i+1:
                x.next = mem[x][i]
            else:
                x.next = None
            g=""
            for elem in mem[x]:
                g+=str(elem.val)
            print(x.val,g)
            if x.next is not None:
                x.next.next = t
                x=x.next.next
            else:
                break
            i+=1
