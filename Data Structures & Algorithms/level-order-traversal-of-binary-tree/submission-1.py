from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque()

        if not root:
            return []
        
        queue.append(root)
        res = []

        while len(queue) > 0:

            limit = len(queue)
            count = 0
            nodes_at_same_level = []
            while count < limit:
                front = queue[0]
                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)
                cur_node = queue.popleft()
                nodes_at_same_level.append(cur_node.val)
                count += 1
            res.append(nodes_at_same_level)

        return res


        