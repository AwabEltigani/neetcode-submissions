# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        

        state = [0,10001,0]

        def bfs(root):
            
            
            if not root or state[1] != 10001 :
                return None

            left = bfs(root.left)

            if left:
                state[0] += 1
                if state[0] == k:
                    state[2] = left.val
                    return
                
            state[0] += 1
            if state[0] == k:
                state[2] = root.val
                return

            right = bfs(root.right)
            if right:
                if state[0] == k:
                    state[2] = right.val
                    return
            
        bfs(root)

        return state[2]


