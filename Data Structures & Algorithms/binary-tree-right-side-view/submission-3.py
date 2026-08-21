# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        res = []

        while queue:
            queue_size = len(queue)
            last_node = None
            for _ in range(queue_size):
                last_node = queue[0]
                if last_node.left is not None:
                    queue.append(last_node.left)
                if last_node.right is not None:
                    queue.append(last_node.right)
                queue.popleft()
            
            res.append(last_node.val)
        
        return res