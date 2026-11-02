class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = {}

        for e1,e2 in edges:
            if e1 not in adj:
                adj[e1] = [e2]
            else:
                adj[e1].append(e2)
            if e2 not in adj:
                adj[e2] = [e1]
            else:
                adj[e2].append(e1)
        
        visited = set()
        def dfs(parent,node):
            if node in visited:
                return False
            if node not in adj:
                return True
            
            visited.add(node)

            for n in adj[node]:
                if n != parent and not dfs(node,n):
                    return False
            
            return True
        
        return (dfs(-1,0) if len(edges) > 0 else True) and (n==len(visited) if len(edges) > 0 else True)

            