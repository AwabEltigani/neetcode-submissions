# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Given a list like 1,2,3,4 with n=2 to remove we are should return 1,2,4
        we can start with a dummy node connected to the list so we can avoid edge cases
        when there is only one node in the list

        1st we create a dummy node
        have a prev pointer to dummy
        cur to the beginning of the list
        count to keep track of the number of node we are currently on
       

        we can start a while loop with a check where we check if count == n
        that is when the cur == the node we are removing when that happens we just do
        prev.next = cur.next
        and return the head

        1,2,3,4
        -1,1,2,3,4

        prev = -1
        cur = 1
        count = 1
        n = 2 

        we can start the loop with
        prev = cur
        cur = cur.next
        count += 1

        prev = 1
        cur = 2
        count = 2

        prev = 2
        cur = 3
        count = 3

        since count == n

        if cur.next == None

        we can just have prev.next = None
        if cur.next != None the we can have
        prev.next = cur.next
        """

        prev = ListNode(-1,head)
        
        cur = head
        if n == 1 and cur.next is None:
            return None
        
        
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

    
        
        

        
        

        
        
