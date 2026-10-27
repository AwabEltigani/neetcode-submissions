class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        def find(node):
            while parent[node] != node:
                node = parent[node]
            return node
        
        def union(n1,n2):
            parent_1 = find(n1)
            parent_2 = find(n2)
            if parent_1 == parent_2:
                return False
            if rank[parent_1] > rank[parent_2]:
                parent[parent_2] = parent_1
                rank[parent_1] += rank[parent_2]
            else:
                parent[parent_1] = parent_2
                rank[parent_2] += rank[parent_1]
            return True
        
        for n1,n2 in edges:
            possible = union(n1,n2)
            if possible:
                n -= 1
        

        return n
            
        