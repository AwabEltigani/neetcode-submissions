# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        r = head
        t = head

        if not head:
            return False

        if head.next and head.next.next:
            r = r.next.next
            t = t.next
        else:
            return False

        if r == t:
            return True

        while r.next and r.next.next:
            r = r.next.next
            if r == t:
                return True
            t = t.next
        
        return False
            
            