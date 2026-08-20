# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def is_p_and_q(self,root,p_found,q_found,node_found):


        if root is None:
            return [False,False,None]
        
        
        
        res = [False,False,None]
        
        left_subtree = self.is_p_and_q(root.left,p_found,q_found,node_found)
        right_subtree = self.is_p_and_q(root.right,p_found,q_found,node_found)

        if left_subtree[2] is not None:
            return [True,True,left_subtree[2]]
        
        if right_subtree[2] is not None:
            return [True,True,right_subtree[2]]
        

        if left_subtree[0] or right_subtree[0]:
            res[0] = True
        
        if left_subtree[1] or right_subtree[1]:
            res[1] = True
        
        if root.val == q.val:
            res[1] = True
        
        if root.val == p.val:
            res[0] = True
        
        if res[0] and res[1]:
            res[2] = root
        
        return res
    
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val == p.val or root.val == q.val:
            return root
        
        root_tree = self.is_p_and_q(root,False,False,None)
        
        return root_tree[2]

        
        





        


    
    