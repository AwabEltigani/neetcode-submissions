# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        

        #find the length
        lengthOfList = 0

        p = head

        while p:
            p = p.next
            lengthOfList = lengthOfList + 1

        #find the split

        lengthOfHalfList = (lengthOfList/2)-1

        p = head
        h = head.next

        i = 0

        while i < lengthOfHalfList:
            p = p.next
            h = h.next
            i = i + 1
        
        p.next = None

        hprev = None
        hcur = h

        while hcur:
            hnext = hcur.next
            hcur.next = hprev
            hprev = hcur
            hcur = hnext
            

        h = hprev
        h2 = head
        hnext = h
        h2next = h2

        while hnext and h2next:
           h2next = h2.next
           h2.next = h
           h2 = h2next
           hnext = h.next
           h.next = h2
           h = hnext
           
           
           
        
        

        

        

        
        

        

        
        