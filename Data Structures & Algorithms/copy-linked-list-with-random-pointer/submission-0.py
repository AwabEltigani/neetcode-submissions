"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head is None:
            return None
        
        hashMap = {}

        dummy = head
        
        newList = Node(0,None,None)
        newListHead = newList
        pointerTo2ndList = newListHead
        
        while dummy is not None:
            newNode = Node(dummy.val,None,None)
            newListHead.next = newNode
            newListHead = newNode
            hashMap[dummy] = newNode
            dummy = dummy.next
        
        newListHead = pointerTo2ndList.next
        dummy = head

        
        while dummy is not None :
            if dummy.random is None:
                newListHead.random = None
            else:
                newListHead.random = hashMap.get(dummy.random)
            dummy = dummy.next
            newListHead = newListHead.next 

        newListHead = pointerTo2ndList.next

        return newListHead

        
        
