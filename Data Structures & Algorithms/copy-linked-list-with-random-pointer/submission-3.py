"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

"""
-create a hashmap why? to store they values as keys with the random pointer values as values

so -{
    3 : null,
    7: 5,
    4: 3,
    5: 7
    }
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        dummy_mine = Node(0,None,None)
        head_mine = dummy_mine
        
        dummy_theirs = head
        old_to_copy = {}

        index = 0
        while dummy_theirs:
            cur_val = dummy_theirs.val
            new_node = Node(cur_val,None,None)
            old_to_copy[dummy_theirs] = new_node
            dummy_theirs = dummy_theirs.next

        dummy_theirs = head
        while dummy_theirs:
            cur = old_to_copy.get(dummy_theirs)
            cur.next = old_to_copy.get(dummy_theirs.next)
            cur.random = old_to_copy.get(dummy_theirs.random)
            dummy_theirs = dummy_theirs.next
        
        return old_to_copy.get(head)
        
        



        






















        