# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) == 0:
            return None
        
        if len(lists) == 1:
            return lists[0]
        
        """
        [[1,2,4]
         [1,3,5]
         [3,6]] -> [1,1,2,3,3,4,5,6]    

        we can create a dummy node that can create the list
        instead of scanning the list to see how many items are in the arrays and stopping when we reach it 
        we can start by having the minimum as -10001 because that is the min value that can be in the lists 
        we can check if a list is None we can skip and if all lists are none the min doesnt change meaning that    we reached the end of the loop

        the algorith i will use is by checking minimum of each list and what list it is since there could be dupelicate minimum values 

        we can start by having the minimum being -10001
        in the first iteration the values will be 1,1,3
        but we will save that the value is 1,0 1 is the min and 0 is the index it is in 
        then we can connect the dummy to the node and we can the head to the next value 
        then we will have 2,1,3
        1 will be next and we can keep doing this until the end of the lists 
        """

        def mergeTwoLinkedLists(linked_list1,linked_lists2):
            newNode = ListNode()
            newHead = newNode
            while linked_list1 and linked_lists2:
                if linked_list1.val > linked_lists2.val:
                    newNode.next = linked_lists2
                    newNode = linked_lists2
                    linked_lists2 = linked_lists2.next
                else:
                    newNode.next = linked_list1
                    newNode = linked_list1
                    linked_list1 = linked_list1.next
                
            if linked_list1:
                newNode.next = linked_list1
                
            if linked_lists2:
                newNode.next = linked_lists2
            
            return newHead.next
            
        while len(lists) > 1:
            merged_lists = []

            for i in range(0,len(lists),2):
                new_list = mergeTwoLinkedLists(lists[i],lists[i + 1] if i + 1 < len(lists) else None)
                merged_lists.append(new_list)
            
            lists = merged_lists
        
        return lists[0]

            

        
        
      
        return lists[-1]






















