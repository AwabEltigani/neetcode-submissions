# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return None
        
        if k == 1:
            return head
        
        cur_k = 1

        cur_head = head
        while cur_head and k > cur_k:
            cur_head = cur_head.next
            cur_k += 1
        if not cur_head:
            return head
        
        res = cur_head

        cur_head = head
        last_tail = None
        cur_tail = head

        while True:
            cur_k = 1
            while cur_tail and k > cur_k:
                cur_tail = cur_tail.next
                cur_k += 1
            
            if not cur_tail:
                last_tail.next = cur_head
                break
            
            cur = cur_head
            prev = None
            next_ = cur_head.next
            next_list = cur_tail.next
            cur_tail.next = None

            

            while next_:
                cur.next = prev
                prev = cur
                cur = next_
                next_ = next_.next
            
            cur_tail.next = prev

            
           
            
            if last_tail:
                last_tail.next = cur_tail
            last_tail = cur_head
            cur_head = next_list
            cur_tail = cur_head

        return res
            
            

