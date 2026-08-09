# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        1,2,3 -> 321
        4,5,6 -> 654
        5,7,9 -> 975

        9 -> 9
        1,9 -> 91

        0->0->1 -> 100

        9+91  100
        10%10 = 0
        10//10 = 1
        
        """

        res = ListNode(-1,None)
        dummy = res
        carry = 0

        while l1 and l2:
            val_1 = l1.val
            val_2 = l2.val

            total = val_1 + val_2 + carry

            down = total % 10
            carry = total // 10

            res.next = ListNode(down,None)
            res = res.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            total = l1.val + carry

            down = total % 10
            carry = total // 10

            res.next = ListNode(down,None)
            res = res.next
            l1=l1.next
        
        while l2:
            total = l2.val + carry

            down = total % 10
            carry = total // 10

            res.next = ListNode(down,None)
            res = res.next
            l2=l2.next
        
        if carry > 0:
            res.next = ListNode(carry,None)
            res = res.next

        return dummy.next






