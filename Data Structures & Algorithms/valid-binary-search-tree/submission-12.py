# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root.left and not root.right:
            return True
        
        res = []

        def validBST(root):

            if root is None:
                return None        
            
            left = validBST(root.left)

            if left:
                res.append(left.val)

            root_value = root.val
            res.append(root.val)

            right = validBST(root.right)

            if right:
                res.append(right.val)

            
        leftSubtree = validBST(root)

        for i in range(1,len(res)):
            if res[i - 1] >= res[i]:
                return False
        
        return True

        

        

        




                








        
