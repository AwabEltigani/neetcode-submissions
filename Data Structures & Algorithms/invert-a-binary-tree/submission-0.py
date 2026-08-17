# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return None
        
        left_sub_tree = self.invertTree(root.left)
        right_sub_tree = self.invertTree(root.right)

        if left_sub_tree is None and right_sub_tree is None:
            return root
        
        root.right = left_sub_tree
        root.left = right_sub_tree

        return root

        