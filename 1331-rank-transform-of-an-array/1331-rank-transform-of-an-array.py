class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ans = []
        ls = sorted(arr)
        rank = 1
        dic = {}
        for a in ls:
            if a not in dic:
                dic[a] = rank
                rank += 1
        
        for a in arr:
            ans.append(dic[a])
            
        return ans
                
        