class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj_list = {}
        for pre,post in prerequisites:
            if pre not in adj_list:
                adj_list[pre] = [post]
            else:
                adj_list[pre].append(post)
        
        done = set()
        taken = set()
        res = []

        def dfs(node):
            if node in done:
                return True
            if node in taken:
                return False
            if not adj_list.get(node):
                done.add(node)
                res.append(node)
                return True
            taken.add(node)
            for n in adj_list.get(node):
                if not dfs(n):
                    return False
            done.add(node)
            res.append(node)
            return True

        for key in adj_list:
            if not dfs(key):
                return []
                
        for n in range(numCourses):
            if n not in done:
                res.append(n)
        return res



