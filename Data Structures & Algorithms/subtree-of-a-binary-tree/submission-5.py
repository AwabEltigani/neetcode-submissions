# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def areSameTree(tree1,tree2):
            queue1 = deque([tree1])
            queue2 = deque([tree2])
            while queue1 and queue2:
                cur_node_1 = queue1.popleft()
                cur_node_2 = queue2.popleft()

                if cur_node_1.val != cur_node_2.val:
                    return False
                
                
                if cur_node_1.left:
                    queue1.append(cur_node_1.left)
                
                if cur_node_1.right:
                    queue1.append(cur_node_1.right)
                
                if cur_node_2.left:
                    queue2.append(cur_node_2.left)
                
                if cur_node_2.right:
                    queue2.append(cur_node_2.right)


            if not queue1 and queue2:
                return False
            
            if queue1 and not queue2:
                return False
                
        
            return True
            


        
        subTree_root_val = subRoot
        queue = deque([root])
        cur_node = None
        res = []
        while queue:
            cur_node = queue.popleft()
            if cur_node.val == subRoot.val:
                areTheSameTree = areSameTree(cur_node,subRoot)
                if areTheSameTree:
                    return True
            
            if not cur_node.left and not cur_node.right:
                continue
            
            if cur_node.left:
                queue.append(cur_node.left)
            
            if cur_node.right:
                queue.append(cur_node.right)
        
        if not res:
            return False
        
        tree1 = res[-1]
        tree2 = subRoot

        print(cur_node.val,subRoot.val)


        
        print(tree1,tree2)

        

