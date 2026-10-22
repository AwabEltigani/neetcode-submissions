class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        prereq = {}
        done = set()

        for pre,post in prerequisites:
            if pre not in prereq:
                prereq[pre] = [post]
            else:
                prereq.get(pre).append(post)
        taken = set()
        def dfs(course):
            if course in taken:
                return False
            taken.add(course)
            if not prereq.get(course) or course in done:
                return True
            for c in prereq.get(course):
                if not dfs(c):
                    return False
                taken.remove(c)
            
            return True
        
        for c in prereq:
            if not dfs(c):
                return False
            taken.remove(c)
            done.add(c)

        
        return True
            
