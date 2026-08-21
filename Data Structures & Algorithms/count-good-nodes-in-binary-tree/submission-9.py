# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def goodNodes(self, root: TreeNode) -> int:
        self.good_node_count = 1
        self.countGoodNodes(root.left,root.val)
        self.countGoodNodes(root.right,root.val)

        return self.good_node_count
        
    def countGoodNodes(self,cur_node,cur_max):
        
        if cur_node is None:
            return 0
        
        
        if cur_node.val >= cur_max:
            self.good_node_count += 1
            cur_max = cur_node.val

        self.countGoodNodes(cur_node.left,cur_max)
        self.countGoodNodes(cur_node.right,cur_max)

        

        
    

        
