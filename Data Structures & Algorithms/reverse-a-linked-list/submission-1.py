# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        prev = None
        cur = head
        next_cur = head.next

        while next_cur:
            cur.next = prev
            prev = cur
            cur = next_cur
            next_cur = next_cur.next
        
        cur.next = prev
        
        return cur