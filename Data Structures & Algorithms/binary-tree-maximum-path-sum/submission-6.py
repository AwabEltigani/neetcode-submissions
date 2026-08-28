# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        cur_max = [-100000000000000000]
        def findMaxPath(root):
            if root is None:
                return -100000000000000

            left = max(findMaxPath(root.left), 0)
            right = max(findMaxPath(root.right), 0)
            cur_max[0] = max(cur_max[0], root.val + left + right)
            return root.val + max(left, right)
        
        findMaxPath(root)

        return cur_max[0]
    

        


        