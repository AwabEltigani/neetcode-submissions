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
            if node in c:
                return 
            c[node] = Node(node.val)
            for n in node.neighbors:
                dfs(n)
                c[node].neighbors.append(c.get(n))
        dfs(node)
        print(c)
        return c.get(node)
        m = {}
        for n in c.keys():               
            m[n] = Node(n)
        
        for k,v in m.items():
            v.neighbors.extend(m.get(node) for node in c.get(k))

        return m.get(node.val)
        
       
        

        
        
        
                







