"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
       
        c = {}
        if node is None:
            return None

        def dfs(node):
            if node.val in c or node.neighbors is None:
                return 
            c[node.val] = [n.val for n in node.neighbors]
            for n in node.neighbors:
                dfs(n)
        dfs(node)
        m = {}
        for n in c.keys():               
            m[n] = Node(n)
        
        for k,v in m.items():
            v.neighbors.extend(m.get(node) for node in c.get(k))

        return m.get(node.val)
        
       
        

        
        
        
                







