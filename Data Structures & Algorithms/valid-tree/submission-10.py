class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        
        adj = {}
        first_element = -1
        for a,b in edges:
            if first_element == -1:
                first_element = a
            if a not in adj:
                adj[a] = [b]
            else:
                adj[a].append(b)
            if b not in adj:
                adj[b] = [a]
            else:
                adj[b].append(a)
        
        
            
  
        seen = set()
        done = set()

        def dfs(node,parent):
            if node in seen:
                return False
            seen.add(node)
            if node not in adj:
                return True
            for n in adj[node]:
                if n == parent:
                    continue
                if not dfs(n,node):
                    return False
            
            return True
        
        res = dfs(first_element,-1)

        

        return res and n==len(seen)
            