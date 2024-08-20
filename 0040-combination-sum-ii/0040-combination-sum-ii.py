class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def dfs(idx, path, total):
            if total == target:
                new = path.copy()
                ans.append(new)
                return
            if idx >= len(candidates) or total > target:
                return
            
            path.append(candidates[idx])
            dfs(idx+1, path, total+candidates[idx])
            path.pop()
            
            while idx+1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx = idx + 1
            dfs(idx+1, path, total)
        
        dfs(0, [], 0)
        return ans
        