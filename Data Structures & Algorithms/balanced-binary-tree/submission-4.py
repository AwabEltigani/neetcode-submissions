# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        leftSubtree = self.checkBalancedSubtree(root.left)
        rightSubtree = self.checkBalancedSubtree(root.right)
        print(leftSubtree,rightSubtree)

        if leftSubtree[1] and rightSubtree[1]:
            diff = abs(leftSubtree[0]-rightSubtree[0])
            return False if diff > 1 else True
        
        return False
    
    def checkBalancedSubtree(self,root):
        if root is None:
            return [0,True]
        
        leftSubtree = self.checkBalancedSubtree(root.left)
        rightSubtree = self.checkBalancedSubtree(root.right)
        print(leftSubtree,rightSubtree)

        diff = abs(leftSubtree[0]-rightSubtree[0])

        isBalancedTree = False if diff > 1 else True

        return [max(leftSubtree[0],rightSubtree[0]) + 1,isBalancedTree]
        