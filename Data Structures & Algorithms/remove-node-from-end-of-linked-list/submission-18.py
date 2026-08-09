# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        prev = ListNode(-1,head)
        dummy = prev
        
        cur = head
        
        
        
        end = head
        
        count = 0

        while count < n:
            end = end.next
            count += 1
        
        
        while end:
            prev = prev.next
            end = end.next
        
  
            
        prev.next = prev.next.next
        
        return dummy.next

    
        
        

        
        

        
        
