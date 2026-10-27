class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]

        for a,b in edges:
            root_a = a
            while root_a != parent[root_a]:
                root_a = parent[root_a]
            root_b = b
            while root_b != parent[root_b]:
                root_b = parent[root_b]
            if root_a == root_b:
                continue
            if rank[root_a] >= rank[root_b]:
                rank[root_a] += rank[root_b]
                parent[root_b] = root_a
                n -= 1
            else:
                rank[root_b] += rank[root_a]
                parent[root_a] = root_b
                n -= 1
        print(parent)
        print(rank)
        return n



        
            
      
        
            
