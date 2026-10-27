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
            if rank[root_a] >= rank[root_b]:
                rank[root_a] += rank[root_b]
            if root_a == root_b:
                continue
                for i in range(len(parent)):
                    if parent[i] == root_b:
                        parent[i] = root_a
            else:
                rank[root_b] += rank[root_a]
                for i in range(len(parent)):
                    if parent[i] == root_a:
                        parent[i] = root_b
                parent[root_a] = root_b
        
        print(parent)
        print(rank)
        
        return len(set(parent))



        
            
      
        
            
