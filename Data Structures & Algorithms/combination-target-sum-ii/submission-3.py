class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        data = []
        candidates.sort()

        def dfs(index,total):
            if total == target:
                res.append(data.copy())
            if total >= target:
                return 
            prev = -1
            for i in range(index,len(candidates)):
                if candidates[i] == prev:
                    continue
                data.append(candidates[i])
                total += candidates[i]
                dfs(i + 1,total)
                data.pop()
                total -= candidates[i]
                prev = candidates[i]
        dfs(0,0)
        return res
                