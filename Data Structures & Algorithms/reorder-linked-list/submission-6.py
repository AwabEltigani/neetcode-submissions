# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        """
        0,1,2,3,4,5,6
        scan the list to get the size 
        size here is 7 
        one we find it we break the list into 2 lists math.ceil(size / 2) = 4
        0,1,2,3 and the other will be 4,5,6
        once we get that what we do is reverse the second list 
        so it becomses 6,5,4
        then we connect them 0,6,1,5,2,4,3

        2,4,6,8

        size = 4 
        half = size/2 = 2

        first_half = 2,4
        second_half = 6,8

        reverse second_half = 8,6

        then connect 

        2,8,4,6 
        
        """
        

        size = 0

        counter = head
        #to get the size of the list
        while counter:
            size += 1
            counter = counter.next
        if size == 1:
            return

        half = math.ceil(size/2)
        cur_pos = half
        second_half = head
        first_half_tail = ListNode(0,head)
        
        while cur_pos > 0:
            second_half = second_half.next
            first_half_tail = first_half_tail.next
            cur_pos -= 1
        
        first_half_tail.next = None
        
        prev = None
        cur = second_half
        cur_next = second_half.next
        """
        6,8,10
        prev = none
        cur = 6,none
        next = 8

        """
        while cur_next:
            print(cur.val)
            cur_next = cur.next
            cur.next = prev
            prev = cur
            cur = cur_next
        
        second_half = prev if cur is None else cur
        
        
        dummy = ListNode(0,head)
        
        #2 4 
        #8 6 
        #0 -> 2

       
        donut = head

        
        while donut and second_half:
            dummy.next = donut
            dummy = donut
            donut = donut.next
            dummy.next = second_half
            dummy = second_half
            second_half = second_half.next
        
        if donut:
            dummy.next = donut
        if second_half:
            dummy.next = second_half
            
        
        
            

            

        
        

        
        
        