class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        idx, path, total = 0, [], 0
        
        def dfs(idx, path, total):
            if idx == len(candidates) or total > target:
                return
            if total == target:
                ans.append(path.copy())
                return
            
            path.append(candidates[idx])
            dfs(idx, path, total+candidates[idx])
            path.pop()
            dfs(idx+1, path, total)
            
        
        dfs(idx, path, total)
        return ans
        