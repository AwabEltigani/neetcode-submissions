# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        we have to have two pointers for the solution one fast and one slow
        -the fast moves twice forward than the slow
        -fast twice slow ones
        -if fast is ever out of bounce then we return False
        -if fast at any point == to slow then we can return true 
        -since the fast is twice as fast by the time it reaches the end of the 
        the slow will be in the mid point right
        -if fast ever equals to slow other than the start then we return false
        """


        dummy = ListNode(0,head)
        fast = dummy
        slow = dummy

        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        
        return False