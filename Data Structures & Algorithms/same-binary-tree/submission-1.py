from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        


        if not p and not q:
            return True
        
        queue_p = deque([p])
        queue_q = deque([q])

        while queue_p and queue_q:
            
            p_node = queue_p.popleft()
            q_node = queue_q.popleft()



            if (p_node is None and q_node is not None) or (p_node is not None and q_node is None):
                return False
            

            if p_node is None and q_node is None:
                continue
            
            
            if (p_node.left is None and q_node.left) or (q_node.left is None and q_node.left):
                return False
            
            if (p_node.right is None and q_node.right) or (q_node.right is None and q_node.right):
                return False
            
            if p_node.val != q_node.val:
                return False
            
            queue_p.append(p_node.left)
            
            
            
            queue_p.append(p_node.right)
            
            
            queue_q.append(q_node.left)
            
            queue_q.append(q_node.right)
        
        
        return True
        
