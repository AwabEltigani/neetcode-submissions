# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global max_diameter
        max_diameter = 0
        
        res = self.diameterOfBinaryTree2(root)

        return max_diameter

    def diameterOfBinaryTree2(self, root: Optional[TreeNode]) -> int:
        global max_diameter

        if root is None:
            return 0
        
        left_subtree = self.diameterOfBinaryTree2(root.left)
        right_subtree = self.diameterOfBinaryTree2(root.right)
        
        max_diameter = max(max_diameter,left_subtree + right_subtree)

        return 1 + max(left_subtree,right_subtree)


        