class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = {}
        for a,b in edges:
            if a not in adj:
                adj[a] = [b]
            else:
                adj[a].append(b)
            if b not in adj:
                adj[b] = [a]
            else:
                adj[b].append(a)
            
        print(adj)
        
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

        

        return dfs(0,-1) and n==len(seen)
            