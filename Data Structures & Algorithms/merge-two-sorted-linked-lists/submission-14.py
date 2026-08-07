# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        
        if list1 is None and list2 is None:
            return None

        if list1 is None:
            return list2

        if list2 is None:
            return list1
        
        if list2.val < list1.val:
            list1,list2 = list2,list1
        
        if list1.next is None and list2.next is None:
            list1.next = list2
            return list1
        
        output = ListNode(100,list1)
        cur_pos = output

        while list1 and list2:
            if list1.val < list2.val:
                cur_pos.next = list1
                cur_pos = list1
                list1 = list1.next
            else:
                cur_pos.next = list2
                cur_pos = list2
                list2 = list2.next
        if list1:
            cur_pos.next = list1
        if list2:
            cur_pos.next = list2
        return output.next
           



        
        
