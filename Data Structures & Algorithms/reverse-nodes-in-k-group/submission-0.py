# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        1,2,3,4,5,6
        cur_head = head
        cur_k = 1
        cur_tail = cur_head
        next_list = 4

        cur_tail = 3
        cur_k = 3
        next_list = 4
        1)while cur_tail and cur_k < k:
            cur_tail = cur_tail.next
            cur_k += 1
        next_list = cur_tail.next

        2)reverse the list using cur_head
        3)cur_head will be at the end so we can do cur_head.next = next_list and keep doing this till the whole linkedlist is reversed
        if cur_k < k then we break

        time_complexity = O(n)
        space = O(1)
        """

        res = head
        cur_k = 1
        

        while res and cur_k < k:
            res = res.next
            cur_k += 1
        
        if not res:
            return head
        
        cur_k = 1
        cur_head = head
        cur_tail = head
        next_list = None
        last_tail = None
        

        while True:
            cur_k = 1
            if not cur_tail:
                break
            
            while cur_tail.next and cur_k < k:
                cur_tail = cur_tail.next
                cur_k += 1

            if cur_k < k:
                last_tail.next = cur_head
                break
            
  
            
            if cur_tail.next:
                next_list = cur_tail.next
            else:
                next_list = None
                
            cur_tail.next = None
            
            cur = cur_head
            head_cur = cur
            prev = None
            next_ = cur.next
        
        
            while next_:
                cur.next = prev
                prev = cur
                cur = next_
                next_ = next_.next
            
            
            if last_tail:
                last_tail.next = cur_tail
            cur_tail.next = prev
            last_tail = cur_head
            cur_head = next_list
            cur_tail = cur_head
            
            
            
            


        return res

        

