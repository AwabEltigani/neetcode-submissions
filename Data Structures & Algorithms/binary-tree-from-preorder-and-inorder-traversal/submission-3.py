# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if len(inorder) == 1:
            return TreeNode(inorder[0],None,None)
        
        value_to_index = {}

        for i in range(len(inorder)):
            value_to_index[inorder[i]] = i
        
        def dfs(rootIndex,left,right):

            cur_root = TreeNode(preorder[rootIndex],None,None)

            index_in_inorder = value_to_index.get(preorder[rootIndex])

            if left < index_in_inorder:
                cur_root.left = dfs(rootIndex + 1,left,index_in_inorder - 1)

            left_size = index_in_inorder - left

            if right > index_in_inorder:
                cur_root.right = dfs(rootIndex + left_size + 1,index_in_inorder + 1,right)
            
            return cur_root

        return dfs(0,0,len(inorder) - 1)









        