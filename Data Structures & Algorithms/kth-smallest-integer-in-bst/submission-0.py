# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        res = []

        

        def bfs(root):

            if not root:
                return None

            left = bfs(root.left)

            if left:
                res.append(left.val)
            
            res.append(root.val)

            right = bfs(root.right)

            if right:
                res.append(right.val)
            
        bfs(root)

        return res[k-1]


