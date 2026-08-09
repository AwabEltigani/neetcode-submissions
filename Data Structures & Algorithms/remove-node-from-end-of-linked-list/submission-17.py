# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        prev = ListNode(-1,head)
        
        cur = head
        
        
        
        dummy = head
        dummy_2 = dummy
        count = 0

        while count < n:
            dummy = dummy.next
            count += 1
        
        cur = head
        
        

        while dummy:
            prev = prev.next
            cur = cur.next
            dummy = dummy.next
        
  
        if prev.val == -1:
            prev.next = cur.next
            return prev.next
            
        prev.next = cur.next
        cur.next = None
        return head

    
        
        

        
        

        
        
