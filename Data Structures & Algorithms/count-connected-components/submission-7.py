class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        res = [[] for _ in range(n)]
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
        
        
        seen = set()
        
        res = [0]
        print(adj)
        def dfs(node):
            seen.add(node)
            if node not in adj:
                return 
            for n in adj[node]:
                if n not in seen:
                    dfs(n)
        res = 0
        for num in range(n):
            if num not in seen:
                res += 1
                dfs(num)
        
        return res

        
            
            
        

