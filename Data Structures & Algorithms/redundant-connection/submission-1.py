class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        parent = [i for i in range(len(edges) + 2)]
        rank = [1 for _ in range(len(edges) + 2)]
        
        def find(node):
            while node != parent[node]:
                node = parent[node]
            return node
        
        def union(n1,n2):
            root1 = find(n1)
            root2 = find(n2)

            if root1 == root2:
                return 
            
            if rank[root1] >= rank[root2]:
                parent[root2] = root1
                rank[root1] += rank[root2]
            else:
                parent[root1] = root2
                rank[root2] += rank[root1]
        res = ()
        for i in range(len(edges)):
            if find(edges[i][0]) == find(edges[i][1]):
                return [edges[i][0],edges[i][1]]
            union(edges[i][0],edges[i][1])
        

            
            
        
                
        

            
            
            